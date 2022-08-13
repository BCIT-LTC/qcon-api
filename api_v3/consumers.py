import json
from channels.generic.websocket import JsonWebsocketConsumer
from django.core.files.base import ContentFile
import base64

from .models import Question, Section, QuestionLibrary, \
    Image, MultipleChoice, MultipleChoiceAnswer, TrueFalse, Fib, MultipleSelect, MultipleSelectAnswer, \
        Matching, MatchingAnswer, MatchingChoice, Ordering, WrittenResponse
import re
import logging
logger = logging.getLogger(__name__)
from .logging.contextfilter import QuestionlibraryFilenameFilter

from .serializers import JsonResponseSerializer
from .process.process import Process

class TextConsumer(JsonWebsocketConsumer):

    def connect(self):
        print("connected")
        sessionid = None
        # print(self.scope['url_route']['kwargs']['session_id'])
        self.sessionid = self.scope['url_route']['kwargs']['session_id']
        self.channel_layer.group_add(self.sessionid, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("disconnected")
        self.channel_layer.group_discard(self.sessionid, self.channel_name)
        pass

    def receive_json(self, content, **kwargs):
        logging_filter = None
        new_questionlibrary = None
        p = Process(new_questionlibrary)
###########################################
        # Save the file
###########################################
        try:
            p.questionlibrary = self.save_file(content)
            logging_filter = QuestionlibraryFilenameFilter(p.questionlibrary)
            logger.addFilter(logging_filter)
            logger.info("File Saved")
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(text_data=json.dumps(p.sendformat("Error", "Not a valid .docx File", "")))
            # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))
            return
        
###########################################
        # create_pandocstring
###########################################

        try:
            p.questionlibrary.create_pandocstring()
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(
                text_data=json.dumps(p.sendformat("Error", "File unreadable", "")))
            # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "The file is valid", "")))

###########################################
        # Extract Images
###########################################

        try:
            p.extract_images()
        except ImageExtractError as e:
            self.send(text_data=json.dumps(p.sendformat("Warn", "Images extraction failed", "")))
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Image found: " + str(p.images_extracted), "")))
##########################################
        # run_formatter
##########################################

        try:
            p.run_formatter()
        except:
            logger.error("FormatterError")
            self.send(text_data=json.dumps(p.sendformat("Error", "No contents found in the body of the file", "")))
            # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Content Body detected", "")))

##########################################
        # run_sectioner
##########################################

        try:
            p.run_sectioner()
        except SectionerError as e:
            logger.error("SectionerError: " + str(e))
            self.send(text_data=json.dumps(p.sendformat("Error", "Sections can not be identified", "")))
            # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))         
            return
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Section found: " + str(p.subsection_count), "")))
##########################################
        # run_splitter
##########################################

        try:
            p.run_splitter()
        except SplitterError as e:
            logger.error("SplitterError: " + str(e))
            self.send(text_data=json.dumps(p.sendformat("Error", "Splitter failed", "")))
            # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Question found: " + str(p.questions_expected), "")))
###########################################
        # Grab end answers
###########################################

        try:
            p.get_endanswers()
        except ImageExtractError as e:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Endanswers not found", "")))
        else:
            if p.endanswers_count > 0:
                self.send(text_data=json.dumps(p.sendformat("Busy", "End answers found", "")))

###########################################
        # run_parser
###########################################

        try:
            p.run_parser()
            # run_parser(new_questionlibrary)
        except ParserError as e:
            logger.error("ParserError: " + str(e))
            self.send(text_data=json.dumps(p.sendformat("Error", "Parser failed", "")))
                # close connection
            self.send(text_data=json.dumps(p.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(p.sendformat("Busy", "Parsing complete", "")))

###########################################
        # Add Images back
###########################################

        # select all questions for this QL
        all_questions = Question.objects.filter(section__question_library=p.questionlibrary)
        # select all images for this QL
        all_images = Image.objects.filter(question_library=p.questionlibrary)

        for image in all_images:
            for question in all_questions:
                substring = "&lt;&lt;&lt;&lt;" + str(image.id) + "&gt;&gt;&gt;&gt;"
                question.text = re.sub(substring, lambda x: image.image, question.text)
                question.save()

                #Check MC
                MC_answer_objects = MultipleChoiceAnswer.objects.filter(multiple_choice__question=question)   
                for answer in MC_answer_objects:
                    answer.answer = re.sub(substring, lambda x: image.image, answer.answer)
                    if answer.answer_feedback is not None:
                        answer.answer_feedback = re.sub(substring, lambda x: image.image, answer.answer_feedback)
                    answer.save()
                #Check TF
                TF_object = TrueFalse.objects.filter(question=question)
                for tf in TF_object:
                    tf.true_feedback = re.sub(substring, lambda x: image.image, tf.true_feedback)
                    tf.save()
                #Check FIB
                FIB_object = Fib.objects.filter(question=question)
                for fib_question in FIB_object:
                    fib_question.text = re.sub(substring, lambda x: image.image, fib_question.text)
                    fib_question.save()
                #Check MS
                MS_answer_objects = MultipleSelectAnswer.objects.filter(multiple_select__question=question)   
                for answer in MS_answer_objects:                
                    answer.answer = re.sub(substring, lambda x: image.image, answer.answer)
                    answer.save()
                #Check ORD
                ORD_objects = Ordering.objects.filter(question=question) 
                for ordering in ORD_objects:    
                    if ordering.text is not None:            
                        ordering.text = re.sub(substring, lambda x: image.image, ordering.text)
                    if ordering.ord_feedback is not None:
                        ordering.ord_feedback = re.sub(substring, lambda x: image.image, ordering.ord_feedback)
                    ordering.save()
                #Check MAT answer
                MAT_answer_objects = MatchingAnswer.objects.filter(matching_choice__matching__question=question)
                for mat_answer in MAT_answer_objects:
                    if mat_answer.answer_text is not None:            
                        mat_answer.answer_text = re.sub(substring, lambda x: image.image, mat_answer.answer_text)
                    mat_answer.save()
                #Check MAT choice
                MAT_choice_objects = MatchingChoice.objects.filter(matching__question=question)
                for mat_choice in MAT_choice_objects:
                    if mat_choice.choice_text is not None:            
                        mat_choice.choice_text = re.sub(substring, lambda x: image.image, mat_choice.choice_text)
                    mat_choice.save()
                #Check WR
                WR_objects = WrittenResponse.objects.filter(question=question)
                for wr in WR_objects:
                    if wr.initial_text is not None:        
                        wr.initial_text = re.sub(substring, lambda x: image.image, wr.initial_text)
                    if wr.answer_key is not None:  
                        wr.answer_key = re.sub(substring, lambda x: image.image, wr.answer_key)
                    wr.save()
###########################################
        # count all question level errors
###########################################

        sections = Section.objects.filter(question_library=p.questionlibrary)
        for section in sections:
            questions = Question.objects.filter(section=section)
            for question in questions:
                if question.error is not None:
                    self.question_error_count += 1

                ###### MC ERROR COUNT
                mc = MultipleChoice.objects.filter(question=question)
                try:
                    if mc.error is not None:
                        self.question_error_count += 1

                    mcas = mc.get_multiple_choice_answers()
                    if mca is not None:
                        for mca in mcas:
                            if mca.error is not None:
                                self.question_error_count += 1
                except:
                    pass
                
                ###### TF ERROR COUNT
                try:
                    tf = TrueFalse.objects.filter(question=question)
                    if tf.error is not None:
                        self.question_error_count += 1
                except:
                    pass

                ###### FIB ERROR COUNT
                try:
                    fib = Fib.objects.filter(question=question)
                    if fib.error is not None:
                        self.question_error_count += 1
                except:
                    pass
                ###### MS ERROR COUNT
                try:
                    ms = MultipleSelect.objects.filter(question=question)
                    if ms.error is not None:
                        self.question_error_count += 1

                    msas = ms.get_multiple_select_answers()
                    if msas is not None:
                        for msa in msas:
                            if msa.error is not None:
                                self.question_error_count += 1    
                except:
                    pass
                ###### MAT ERROR COUNT
                try:
                    mat = Matching.objects.filter(question=question)
                    if mat is not None:
                        self.question_error_count += 1
                    
                    mat_choices = mat.get_matching_choices()
                    if mat_choices is not None:
                        for mat_choice in mat_choices:
                            if mat_choice.error is not None:
                                self.question_error_count += 1    

                    mat_answers = mat.get_unique_matching_answers()
                    if mat_answers is not None:
                        for mat_answer in mat_answers:
                            if mat_answer.error is not None:
                                self.question_error_count += 1    
                except:
                    pass
                ###### ORD ERROR COUNT
                try:
                    ord = Ordering.objects.filter(question=question)
                    if ord.error is not None:
                        self.question_error_count += 1    
                except:
                    pass
                ###### WR ERROR COUNT
                try:
                    wr = WrittenResponse.objects.filter(question=question)
                    if wr.error is not None:
                        self.question_error_count += 1  
                except:
                    pass

###########################################
        # serialize and send response
###########################################

        serialized_ql = JsonResponseSerializer(p.questionlibrary)
        self.send(text_data=json.dumps(p.sendformat("Done", "", serialized_ql.data)))

######################### Close Connection
        self.send(text_data=json.dumps(p.sendformat("Close", "", "")))

    def save_file(self, content):
        format, fixeddata = content.get('file').split(';base64,')
        received_file = ContentFile(base64.b64decode(fixeddata),
                                    name=content.get('filename'))
        newfile = QuestionLibrary.objects.create()
        newfile.temp_file = received_file
        newfile.session_id = self.sessionid
        newfile.main_title = content.get('filename').split(".")[0]
        newfile.randomize_answer = content.get('randomize_answer')
        newfile.save()
        return newfile

    def count_question_errors(self, questionlibrary):
        pass
        # if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        #     received_file = ContentFile(base64.b64decode(fixeddata),
        #                                 name=content.get('filename'))
        #     newfile = QuestionLibrary.objects.create()
        #     newfile.temp_file = received_file
        #     newfile.session_id = self.sessionid
        #     newfile.save()
        #     return newfile
        # else:
        #     raise FileValidationError("not a valid *.docx file")

class ImageExtractError(Exception):
    pass

class FileValidationError(Exception):
    pass


class FormatterError(Exception):
    pass


class SectionerError(Exception):
    pass

class SplitterError(Exception):
    pass

class ParserError(Exception):
    pass
