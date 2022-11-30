import json
from channels.generic.websocket import JsonWebsocketConsumer
from django.core.files.base import ContentFile
import base64
import os

from .models import Question, Section, QuestionLibrary, \
    Image, MultipleChoice, MultipleChoiceAnswer, TrueFalse, Fib, MultipleSelect, MultipleSelectAnswer, \
        Matching, MatchingAnswer, MatchingChoice, Ordering, WrittenResponse
import re
import logging
newlogger = logging.getLogger(__name__)
from .logging.logging_adapter import FilenameLoggingAdapter
# from .logging.contextfilter import QuestionlibraryFilenameFilter
# logger.addFilter(QuestionlibraryFilenameFilter())
from api_v3.logging.ErrorTypes import EMFImageError
from .process.process_helper import add_error_message
from .serializers import JsonResponseSerializer
from .process.process import Process

from .process.extract_images import ImageExtractError
from .process.formatter import FormatterError
from .process.sectioner import SectionerError
from .process.splitter import SplitterError
from .process.endanswers import EndAnswerError
from .process.parser import ParserError
from .tasks import MarkDownConversionError

import elasticapm
elastic_client = elasticapm.get_client()

# class FilenameLoggingAdapter(logging.LoggerAdapter):
#     """
#     This example adapter expects the passed in dict-like object to have a
#     'connid' key, whose value in brackets is prepended to the log message.
#     """
#     def process(self, msg, kwargs):
#         return f"[{self.extra['filename']}] {msg}", kwargs

class TextConsumer(JsonWebsocketConsumer):

    def connect(self):
        newlogger.info("New connection started")
        sessionid = None
        # print(self.scope['url_route']['kwargs']['session_id'])
        # self.sessionid = self.scope['url_route']['kwargs']['session_id']
        # self.channel_layer.group_add(self.sessionid, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        self.close()
        newlogger.info("Closing Connection")
        # self.channel_layer.group_discard(self.sessionid, self.channel_name)

    def receive_json(self, content, **kwargs):
        elastic_client.begin_transaction('main')
###########################################
        # Save the file
###########################################
        try:
            newlogger.info("Process Start")
            format, fixeddata = content.get('file').split(';base64,')
            received_file = ContentFile(base64.b64decode(fixeddata),
                                        name=content.get('filename'))

            new_questionlibrary = QuestionLibrary.objects.create()

            new_questionlibrary.temp_file = received_file
            # new_questionlibrary.session_id = self.sessionid
            new_questionlibrary.main_title = content.get('filename').split(".")[0]
            new_questionlibrary.randomize_answer = content.get('randomize_answer')
            new_questionlibrary.user_ip = content.get('user_ip')
            new_questionlibrary.save()
            process = Process(new_questionlibrary)
            logger = FilenameLoggingAdapter(newlogger, {
                'filename': new_questionlibrary.temp_file.name,
                'user_ip': new_questionlibrary.user_ip
                })
            logger.info("File Saved")
        except Exception as e:
            logger.error("Not a valid .docx File: {e}")
            self.send(text_data=json.dumps(process.sendformat("Error", "Not a valid .docx File", "")))
            # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            return
        
###########################################
        # create_pandocstring
###########################################

        try:
            # process.questionlibrary.create_pandocstring()
            process.run_pandoc()
            logger.info("Pandoc Done")
        except Exception as e:
            logger.error(str(e))
            self.send(
                text_data=json.dumps(process.sendformat("Error", "File unreadable", "")))
            # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            # return
        # except Exception as e:
        #     self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
        #     logger.error(str(e))
        #     return
        else:
            self.send(text_data=json.dumps(process.sendformat("Busy", "The file is valid", "")))

###########################################
        # Extract Images
###########################################

        try:
            process.extract_images()
            logger.info("Done extracting Images")
        except ImageExtractError as e:
            self.send(text_data=json.dumps(process.sendformat("Warn", "Images extraction failed", "")))
        else:
            logger.info(f'{str(process.images_extracted)} Images Extracted')
            self.send(text_data=json.dumps(process.sendformat("Busy", "Image found: " + str(process.images_extracted), "")))

###########################################
        # Convert to txt for fixing numbering
###########################################

        try:
            process.convert_txt()
            logger.info("convert txt done")
        except Exception as e:
            logger.error(e)

###########################################
        # Fix Numbering (broken lists)
###########################################

        try:
            process.fix_numbering()
            logger.info("numbering fix done")
        except Exception as e:
            logger.error(e)
            self.send(
                text_data=json.dumps(process.sendformat("Error", str(e), "")))
            # close connection
            # self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            return

##########################################
        # run_formatter
##########################################
        logger.debug("Formatting ...")
        try:
            process.run_formatter()
            logger.info("Formatter Done")
        except FormatterError as e:
            logger.error("FormatterError: " + str(e))
            self.send(text_data=json.dumps(process.sendformat("Error", "No contents found in the body of the file", "")))
            # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(process.sendformat("Busy", "Content Body detected", "")))

##########################################
        # run_sectioner
##########################################
        logger.debug("Sectioning ...")
        try:
            process.run_sectioner()
            logger.info("Sectioner Done")
        except SectionerError as e:
            logger.error("SectionerError: " + str(e))
            self.send(text_data=json.dumps(process.sendformat("Error", "Sections can not be identified", "")))
            # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(process.sendformat("Busy", "Section found: " + str(process.subsection_count), "")))

##########################################
        # run_splitter
##########################################
        logger.debug("Splitting Questions ...")
        try:
            process.run_splitter()
            logger.info("Splitter Done")
        except Exception as e:
            logger.error("SplitterError: " + str(e))
            self.send(text_data=json.dumps(process.sendformat("Error", "Splitter failed", "")))
            # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(process.sendformat("Busy", "Question found: " + str(process.questions_expected), "")))
###########################################
        # Grab end answers
###########################################
        logger.debug("Checking Endanswer ...")
        try:
            process.get_endanswers()
            logger.info("Check Endanswer Done")
        except EndAnswerError as e:
            logger.error("EndAnswerError: " + str(e))
            self.send(text_data=json.dumps(process.sendformat("Busy", "Endanswers not found", "")))
        else:
            if process.endanswers_count > 0:
                self.send(text_data=json.dumps(process.sendformat("Busy", "End answers found", "")))

###########################################
        # run_parser
###########################################
        logger.debug("Starting Parser ...")
        try:
            process.run_parser()
            logger.info("Parser Done")
        except Exception as e:
            logger.error("ParserError: " + str(e))
            self.send(text_data=json.dumps(process.sendformat("Error", "Parser failed", "")))
                # close connection
            self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
        else:
            self.send(text_data=json.dumps(process.sendformat("Busy", "Parsing complete", "")))

###########################################
        # Add Images back
###########################################
        try:
            logger.debug("Adding Images Back: Select all Images ...")
            # select all images for this QL
            all_images = Image.objects.filter(question_library=process.questionlibrary)
            logger.debug("Adding Images Back: Select all Sections ...")
            # select all sections for this QL
            all_sections = Section.objects.filter(question_library=process.questionlibrary)
            logger.debug("Adding Images Back: Check each image for EMF ...")
            for image in all_images:
                section_img_src = image.image
                section_emf_image = False

                if re.match(r"\<img\s+src\=\"data\:image\/x\-emf\;" ,section_img_src):
                    section_emf_image = True
                for section in all_sections:
                    if section.text :
                        substring = "&lt;&lt;&lt;&lt;" + str(image.id) + "&gt;&gt;&gt;&gt;"

                        try:
                            if section_emf_image:
                                error_message = "EMF image format is NOT supported. Please replace this image with JPG or PNG format."
                                section_img_src = f'<img src="media/broken-image.emf" alt="BROKEN IMAGE" style="color:red; font-size:2em;">'
                                add_error_message(section, error_message)
                                raise EMFImageError(section.error)
                        except Exception as e:
                            logger.error(e)
                            # raise Exception(e)

                        section.text = re.sub(substring, lambda x: section_img_src, section.text)
                        section.save()
            
            # select all questions for this QL
            all_questions = Question.objects.filter(section__question_library=process.questionlibrary)
            for image in all_images:
                img_src = image.image
                emf_image = False

                if re.match(r"\<img\s+src\=\"data\:image\/x\-emf\;" ,img_src):
                    emf_image = True
                for question in all_questions:
                    substring = "&lt;&lt;&lt;&lt;" + str(image.id) + "&gt;&gt;&gt;&gt;"
                    try:
                        if emf_image:
                            error_message = "EMF image format is NOT supported. Please replace this image with JPG or PNG format."
                            img_src = f'<img src="media/broken-image.emf" alt="BROKEN IMAGE" style="color:red; font-size:2em;">'
                            add_error_message(question, error_message)
                            raise EMFImageError(question.error)
                    except Exception as e:
                        logger.error(e)
                        # raise Exception(e)

                    question.text = re.sub(substring, lambda x: img_src, question.text)
                    question.save()
                    match(question.questiontype):
                        case 'MC':
                            #Check MC
                            MC_answer_objects = MultipleChoiceAnswer.objects.filter(multiple_choice__question=question)
                            for answer in MC_answer_objects:
                                answer.answer = re.sub(substring, lambda x: img_src, answer.answer)
                                if answer.answer_feedback is not None:
                                    answer.answer_feedback = re.sub(substring, lambda x: img_src, answer.answer_feedback)
                                answer.save()
                        case 'TF':
                            #Check TF
                            TF_object = TrueFalse.objects.filter(question=question)
                            for tf in TF_object:
                                if tf.true_feedback is not None:
                                    tf.true_feedback = re.sub(substring, lambda x: img_src, tf.true_feedback)
                                    tf.save()
                                if tf.false_feedback is not None:
                                    tf.false_feedback = re.sub(substring, lambda x: img_src, tf.false_feedback)
                                    tf.save()
                        case 'FIB' | 'FMB':
                            #Check FIB
                            FIB_object = Fib.objects.filter(question=question)
                            for fib_question in FIB_object:
                                fib_question.text = re.sub(substring, lambda x: img_src, fib_question.text)
                                fib_question.save()
                        case 'MS' | 'MR':
                            #Check MS
                            MS_answer_objects = MultipleSelectAnswer.objects.filter(multiple_select__question=question)
                            for answer in MS_answer_objects:
                                answer.answer = re.sub(substring, lambda x: img_src, answer.answer)
                                if answer.answer_feedback is not None:
                                    answer.answer_feedback = re.sub(substring, lambda x: img_src, answer.answer_feedback)
                                answer.save()
                        case 'ORD':
                            #Check ORD
                            ORD_objects = Ordering.objects.filter(question=question)
                            for ordering in ORD_objects:
                                if ordering.text is not None:
                                    ordering.text = re.sub(substring, lambda x: img_src, ordering.text)
                                if ordering.ord_feedback is not None:
                                    ordering.ord_feedback = re.sub(substring, lambda x: img_src, ordering.ord_feedback)
                                ordering.save()
                        case 'MAT' | 'MT':
                            #Check MAT answer
                            MAT_answer_objects = MatchingAnswer.objects.filter(matching_choice__matching__question=question)
                            for mat_answer in MAT_answer_objects:
                                if mat_answer.answer_text is not None:
                                    mat_answer.answer_text = re.sub(substring, lambda x: img_src, mat_answer.answer_text)
                                mat_answer.save()
                            #Check MAT choice
                            MAT_choice_objects = MatchingChoice.objects.filter(matching__question=question)
                            for mat_choice in MAT_choice_objects:
                                if mat_choice.choice_text is not None:
                                    mat_choice.choice_text = re.sub(substring, lambda x: img_src, mat_choice.choice_text)
                                mat_choice.save()
                        case 'WR' | 'E':
                            #Check WR
                            WR_objects = WrittenResponse.objects.filter(question=question)
                            for wr in WR_objects:
                                if wr.initial_text is not None:
                                    wr.initial_text = re.sub(substring, lambda x: img_src, wr.initial_text)
                                if wr.answer_key is not None:
                                    wr.answer_key = re.sub(substring, lambda x: img_src, wr.answer_key)
                                wr.save()
                    logger.debug("Adding Images Back: Done Replacing images ...")
        except Exception as e:
            logger.error(e)
###########################################
        # count all question level errors
###########################################
        logger.debug("count all question level errors ...")
        sections = process.questionlibrary.get_sections()
        for section in sections:
            questions = Question.objects.filter(section=section)
            for question in questions:
                if question.info is not None:
                    process.question_info_count += 1

                if question.warning is not None:
                    process.question_warning_count += 1

                if question.error is not None:
                    process.question_error_count += 1

                """ ###### MC ERROR COUNT
                mc = MultipleChoice.objects.filter(question=question)
                try:
                    if mc.error is not None:
                        process.question_error_count += 1

                    mcas = mc.get_multiple_choice_answers()
                    if mca is not None:
                        for mca in mcas:
                            if mca.error is not None:
                                process.question_error_count += 1
                except:
                    pass

                ###### TF ERROR COUNT
                try:
                    tf = TrueFalse.objects.filter(question=question)
                    if tf.error is not None:
                        process.question_error_count += 1
                except:
                    pass

                ###### FIB ERROR COUNT
                try:
                    fib = Fib.objects.filter(question=question)
                    if fib.error is not None:
                        process.question_error_count += 1
                except:
                    pass
                ###### MS ERROR COUNT
                try:
                    ms = MultipleSelect.objects.filter(question=question)
                    if ms.error is not None:
                        process.question_error_count += 1

                    msas = ms.get_multiple_select_answers()
                    if msas is not None:
                        for msa in msas:
                            if msa.error is not None:
                                process.question_error_count += 1
                except:
                    pass
                ###### MAT ERROR COUNT
                try:
                    mat = Matching.objects.filter(question=question)
                    if mat is not None:
                        process.question_error_count += 1

                    mat_choices = mat.get_matching_choices()
                    if mat_choices is not None:
                        for mat_choice in mat_choices:
                            if mat_choice.error is not None:
                                process.question_error_count += 1
                    mat_answers = mat.get_unique_matching_answers()
                    if mat_answers is not None:
                        for mat_answer in mat_answers:
                            if mat_answer.error is not None:
                                process.question_error_count += 1
                except:
                    pass
                ###### ORD ERROR COUNT
                try:
                    ord = Ordering.objects.filter(question=question)
                    if ord.error is not None:
                        process.question_error_count += 1
                except:
                    pass
                ###### WR ERROR COUNT
                try:
                    wr = WrittenResponse.objects.filter(question=question)
                    if wr.error is not None:
                        process.question_error_count += 1
                except:
                    pass """

###########################################
        # serialize and send response
###########################################
        logger.info("Process End")

        serialized_ql = JsonResponseSerializer(process.questionlibrary)
        self.send(text_data=json.dumps(process.sendformat("Done", "", serialized_ql.data)))

######################### Close Connection
        self.send(text_data=json.dumps(process.sendformat("Close", "", "")))
        self.close()

        elastic_client.end_transaction('main')
