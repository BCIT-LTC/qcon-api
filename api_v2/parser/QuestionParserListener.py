# Generated from QuestionParser.g4 by ANTLR 4.8
import logging
import re
import pypandoc
from decimal import Decimal
# from api_v2.models import Question, Answer, Fib

from datetime import datetime

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuestionParser import QuestionParser
else:
    from QuestionParser import QuestionParser



# This class defines a complete listener for a parse tree produced by QuestionParser.
class QuestionParserListener(ParseTreeListener):
    def __init__(self, question_library):
        self.questions = []
        self.question = None
        self.answer = None
        self.current_answer_order = 0
        self.question_library = question_library
        self.end_answers = None

    # Return parsed question
    def get_results(self):
        return self.questions

    # Enter a parse tree produced by QuestionParser#parse_question.
    def enterParse_question(self, ctx:QuestionParser.Parse_questionContext):
        pass

    # Exit a parse tree produced by QuestionParser#parse_question.
    def exitParse_question(self, ctx:QuestionParser.Parse_questionContext):
        if self.end_answers == None:
            for question_index, question in enumerate(self.questions):
                self.process_question(question)
                self.question.save()
                # print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
        else:
            for question_index, question in enumerate(self.questions):
                end_answer = self.end_answers[question_index]['answer']
                answers = question.get_answers()
                if len(answers) > 0:
                    if len(answers) == 2:
                        is_true_exist = False
                        is_false_exist = False
                        for answer_obj in answers:
                            answer_body = self.html_to_plain(answer_obj.answer_body).lower().strip()
                            if "true" == answer_body:
                                is_true_exist = True
                            elif "false" == answer_body:
                                is_false_exist = True
                        
                        if is_true_exist == True:
                            if is_false_exist == True:
                                # TF
                                question.question_type = 'TF'
                                question.randomize_answer = False
                                question.correct_answers_length = 1
                                question.save()
                                for answer_obj in answers:
                                    answer_body = self.html_to_plain(answer_obj.answer_body).lower().strip()
                                    if "true" == answer_body:
                                        answer_obj.answer_body = "True"
                                    elif "false" == answer_body:
                                        answer_obj.answer_body = "False"
                                    
                                    if end_answer[0] == answer_obj.prefix[0]:
                                        answer_obj.is_correct = True
                                    answer_obj.save()

                    if question.question_type == None:
                        if ';' in end_answer:
                            end_answers_split = end_answer.split(";")
                            if len(answers) == len(end_answers_split):
                                count_ordering = 0
                                
                                for answer_obj in answers:
                                    answer_obj_text = self.html_to_plain(answer_obj.answer_body).lower().strip()
                                    for end_answer in end_answers_split:
                                        end_answer_text = end_answer.lower().strip()
                                        if end_answer_text == answer_obj_text:
                                            count_ordering = count_ordering + 1
                                
                                if count_ordering == len(end_answers_split):
                                    # ORD
                                    question.question_type = 'ORD'
                                    question.randomize_answer = True
                                    question.save()
                                    for ordering_index, answer in enumerate(answers):
                                        answer.answer_body = end_answers_split[ordering_index]
                                        answer.save()
                        elif ',' in end_answer:
                            end_answers_split = end_answer.split(",")
                            count_ms = 0
                            for answer_obj in answers:
                                answer_obj_prefix = answer_obj.prefix[0].lower()
                                for answer_text in end_answers_split:
                                    end_answer_text = answer_text.lower().strip()
                                    if end_answer_text == answer_obj_prefix:
                                        count_ms = count_ms + 1

                            if count_ms == len(end_answers_split):
                                # MS
                                question.question_type = 'MS'
                                question.correct_answers_length = count_ms
                                question.save()
                                for answer_obj in answers:
                                    answer_obj_prefix = answer_obj.prefix[0].lower()
                                    for answer_text in end_answers_split:
                                        end_answer_text = answer_text.lower().strip()
                                        if end_answer_text == answer_obj_prefix:
                                            answer_obj.is_correct = True
                                            answer_obj.save()
                        else:
                            for answer_obj in answers:
                                answer_obj_prefix = answer_obj.prefix[0].lower()
                                end_answer_text = end_answer.lower().strip()
                                if end_answer_text == answer_obj_prefix:
                                    # MC
                                    question.question_type = 'MC'
                                    question.correct_answers_length = 1
                                    question.save()
                                    answer_obj.is_correct = True
                                    answer_obj.save()

                elif len(answers) == 0:
                    # either MT or WR or FIB
                    is_wr = False
                    fib_answers = question.get_fib_answers()
                    if len(fib_answers) > 0: 
                        # Type FIB
                        question.question_type = 'FIB'
                        question.randomize_answer = False
                        question.save()
                        
                        if ';' in end_answer:
                            # Multi FIB
                            end_answers_split = end_answer.split(";")
                            for answer_index, answer_text in enumerate(end_answers_split):
                                fib_answer = fib_answers[answer_index]
                                fib_answer.text = answer_text
                                fib_answer.save()
                        else:
                            # only one FIB
                            fib_answer = question.get_fib_answers()[0]
                            fib_answer.text = end_answer
                            fib_answer.save()

                        fib_answers = question.get_fib_answers()
                        fib_question_body = question.question_body
                        for index, fib_answer in enumerate(fib_answers):
                            answer_text = "["+ fib_answer.text +"]"
                            fib_question_body = re.sub(r"\[\s*?(\*)+\s*?\]", answer_text, fib_question_body, 1)

                        question.question_body = fib_question_body
                        question.save()
                        
                    elif ';' in end_answer:
                        end_answers_split = end_answer.split(";")
                        
                        count_matching = 0
                        for answer_text in end_answers_split:
                            if '=' in answer_text:
                                count_matching = count_matching + 1

                        if count_matching == len(end_answers_split):
                            # MT
                            question.question_type = 'MT'
                            question.randomize_answer = True
                            question.save()
                            for answer_text in end_answers_split:

                                from api_v2.models import Answer
                                new_answer = Answer()

                                matching_answer = new_answer
                                matching_answer.question = question
                                matching_answer.answer_body = answer_text
                                matching_answer.save()
                        else:
                            is_wr = True
                    else:
                        is_wr = True

                    if is_wr == True:
                        # WR
                        question.question_type = 'WR'
                        question.randomize_answer = False
                        question.save()

                        from api_v2.models import Answer
                        new_answer = Answer()

                        wr_answer = new_answer
                        wr_answer.question = question
                        wr_answer.answer_body = end_answer
                        wr_answer.save()

                self.process_question(question)
                self.question.save()
                # print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
        pass
 
    # Enter a parse tree produced by QuestionParser#section_title.
    def enterSection_title(self, ctx:QuestionParser.Section_titleContext):
        pass

    # Exit a parse tree produced by QuestionParser#section_title.
    def exitSection_title(self, ctx:QuestionParser.Section_titleContext):
        section_name = ctx.getText().replace('##########_SECTION_##########', '')
        section_name = self.markdown_to_plain(section_name)
        section_name = self.trim_text(section_name)
        self.question_library.section_name = section_name
        self.question_library.save()
        pass

    # Enter a parse tree produced by QuestionParser#question.
    def enterQuestion(self, ctx:QuestionParser.QuestionContext):
        from api_v2.models import Question
        new_question = Question()
        self.question = new_question
        self.question.question_library = self.question_library
        self.question.prefix = len(self.questions) + 1
        self.question.save()
        pass

    # Exit a parse tree produced by QuestionParser#question.
    def exitQuestion(self, ctx:QuestionParser.QuestionContext):
        self.questions.append(self.question)
        pass


    # Enter a parse tree produced by QuestionParser#start_question.
    def enterStart_question(self, ctx:QuestionParser.Start_questionContext):
        pass

    # Exit a parse tree produced by QuestionParser#start_question.
    def exitStart_question(self, ctx:QuestionParser.Start_questionContext):
        pass

    # Enter a parse tree produced by QuestionParser#question_header.
    def enterQuestion_header(self, ctx:QuestionParser.Question_headerContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_header.
    def exitQuestion_header(self, ctx:QuestionParser.Question_headerContext):
        pass

    # Enter a parse tree produced by QuestionParser#TypeMc.
    def enterTypeMc(self, ctx:QuestionParser.TypeMcContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMc.
    def exitTypeMc(self, ctx:QuestionParser.TypeMcContext):
        self.question.question_type = 'MC'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeTf.
    def enterTypeTf(self, ctx:QuestionParser.TypeTfContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeTf.
    def exitTypeTf(self, ctx:QuestionParser.TypeTfContext):
        self.question.question_type = 'TF'
        question.randomize_answer = False
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeMs.
    def enterTypeMs(self, ctx:QuestionParser.TypeMsContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMs.
    def exitTypeMs(self, ctx:QuestionParser.TypeMsContext):
        self.question.question_type = 'MS'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeMt.
    def enterTypeMt(self, ctx:QuestionParser.TypeMtContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMt.
    def exitTypeMt(self, ctx:QuestionParser.TypeMtContext):
        self.question.question_type = 'MT'
        question.randomize_answer = True
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeOrd.
    def enterTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOrd.
    def exitTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        self.question.question_type = 'ORD'
        question.randomize_answer = True
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeFib.
    def enterTypeFib(self, ctx:QuestionParser.TypeFibContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeFib.
    def exitTypeFib(self, ctx:QuestionParser.TypeFibContext):
        self.question.question_type = 'FIB'
        question.randomize_answer = False
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeWr.
    def enterTypeWr(self, ctx:QuestionParser.TypeWrContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeWr.
    def exitTypeWr(self, ctx:QuestionParser.TypeWrContext):
        self.question.question_type = 'WR'
        question.randomize_answer = False
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeOther.
    def enterTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOther.
    def exitTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        self.question.question_type = self.ctx.getText()
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#title.
    def enterTitle(self, ctx:QuestionParser.TitleContext):
        pass

    # Exit a parse tree produced by QuestionParser#title.
    def exitTitle(self, ctx:QuestionParser.TitleContext):
        title = self.trim_text(ctx.getText()).split(":")[1]
        title = self.markdown_to_plain(title)
        title = self.trim_text(title)[0:127]
        self.question.title = title
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#points.
    def enterPoints(self, ctx:QuestionParser.PointsContext):
        pass

    # Exit a parse tree produced by QuestionParser#points.
    def exitPoints(self, ctx:QuestionParser.PointsContext):
        points = self.trim_text(ctx.getText()).split(":")[1]
        points = self.markdown_to_plain(points)
        points = self.trim_text(points)
        try:
            points = Decimal(points)
            if points > 0 and points <= 9999:
                self.question.points = points
            else:
                self.question.points = 1.0
                logger = logging.getLogger('api_v2.QuestionParserListener.exitPoints')
                error_message = f"\n310, Points must be greater than 0 and less than or equal to 9,999. \
                              \n\t Points is now set to default 1.0 instead of {points}."
                logger.error(error_message)
            
        except ValueError:
            self.question.points = 1.0
            logger = logging.getLogger('api_v2.QuestionParserListener.exitPoints')
            error_message = f"\n310, Points must be in a decimal format. \
                              \n\t Points is now set to default 1.0 instead of {points}."
            logger.error(error_message)

        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#RandomTrue.
    def enterRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomTrue.
    def exitRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        if self.question.question_type == None or self.question.question_type == 'MC' or self.question.question_type == 'MS':
            self.question.randomize_answer = True
            self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#RandomFalse.
    def enterRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomFalse.
    def exitRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
        if self.question.question_type == None or self.question.question_type == 'MC' or self.question.question_type == 'MS':
            self.question.randomize_answer = False
            self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#question_body.
    def enterQuestion_body(self, ctx:QuestionParser.Question_bodyContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_body.
    def exitQuestion_body(self, ctx:QuestionParser.Question_bodyContext):
        body_text = ""
        for question_content in ctx.content():
            body_text += question_content.getText()
        question_body = self.markdown_to_html(body_text)
        question_body = self.trim_text(question_body)

        if self.question.title == None:
            self.question.title = self.html_to_plain(question_body)[0:127]
        
        if self.question.points == None:
            self.question.points = 1.0

        if self.question.question_type == None or self.question.question_type == 'MC' or self.question.question_type == 'MS':
            if self.question_library.randomize_answer != None:
                self.question.randomize_answer = self.question_library.randomize_answer

        self.question.question_body = question_body

        # print("\n--------------------------QUESTION-------------------------------")
        # print(question_body)

        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            question_feedback = ctx.feedback().getText().lstrip()[1:]
            question_feedback = self.markdown_to_html(question_feedback)
            question_feedback = self.trim_text(question_feedback)
            self.question.question_feedback = question_feedback
        
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#Media.
    def enterMedia(self, ctx:QuestionParser.MediaContext):
        pass

    # Exit a parse tree produced by QuestionParser#Media.
    def exitMedia(self, ctx:QuestionParser.MediaContext):
        pass

    # Enter a parse tree produced by QuestionParser#Hyperlink.
    def enterHyperlink(self, ctx:QuestionParser.HyperlinkContext):
        pass

    # Exit a parse tree produced by QuestionParser#Hyperlink.
    def exitHyperlink(self, ctx:QuestionParser.HyperlinkContext):
        pass

    # Enter a parse tree produced by QuestionParser#FibAnswer.
    def enterFibAnswer(self, ctx:QuestionParser.FibAnswerContext):
        pass

    # Exit a parse tree produced by QuestionParser#FibAnswer.
    def exitFibAnswer(self, ctx:QuestionParser.FibAnswerContext):
        fib_answer = ''
        for fib_content in ctx.ALL_CHARACTER():
            fib_answer += fib_content.getText()
        
        from api_v2.models import Fib
        new_fib = Fib()

        fib = new_fib
        fib.question = self.question
        fib.type = "answer"
        fib.text = self.trim_text(self.markdown_to_plain(fib_answer))
        fib.save()
        pass

    # Enter a parse tree produced by QuestionParser#ContentCharacters.
    def enterContentCharacters(self, ctx:QuestionParser.ContentCharactersContext):
        pass

    # Exit a parse tree produced by QuestionParser#ContentCharacters.
    def exitContentCharacters(self, ctx:QuestionParser.ContentCharactersContext):
        pass

    # Enter a parse tree produced by QuestionParser#feedback.
    def enterFeedback(self, ctx:QuestionParser.FeedbackContext):
        pass

    # Exit a parse tree produced by QuestionParser#feedback.
    def exitFeedback(self, ctx:QuestionParser.FeedbackContext):
        pass

    # Enter a parse tree produced by QuestionParser#ListNoAnswer.
    def enterListNoAnswer(self, ctx:QuestionParser.ListNoAnswerContext):
        self.current_answer_order = 0
        pass

    # Exit a parse tree produced by QuestionParser#ListNoAnswer.
    def exitListNoAnswer(self, ctx:QuestionParser.ListNoAnswerContext):
        self.question.correct_answers_length = None
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#ListWithAnswer.
    def enterListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        self.current_answer_order = 0
        pass
    
    # Exit a parse tree produced by QuestionParser#ListWithAnswer.
    def exitListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        pass

    # Enter a parse tree produced by QuestionParser#list_item.
    def enterList_item(self, ctx:QuestionParser.List_itemContext):
        from api_v2.models import Answer
        new_answer = Answer()
        self.answer = new_answer
        self.answer.question = self.question
        self.answer.is_correct = False
        self.current_answer_order += 1
        self.answer.order = self.current_answer_order
        self.answer.save()
        pass

    # Exit a parse tree produced by QuestionParser#list_item.
    def exitList_item(self, ctx:QuestionParser.List_itemContext):
        prefix = self.trim_text(ctx.list_prefix().getText())
        self.answer.prefix = prefix

        answer_text = ""
        for answer_content in ctx.content():
            answer_text += answer_content.getText()
        answer_body = self.markdown_to_html(answer_text)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body
        
        # print("\n--------------------------LIST ITEM-------------------------------")
        # print(answer_body)

        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            answer_feedback = ctx.feedback().getText().lstrip()[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        
        self.answer.save()
        pass

    # Enter a parse tree produced by QuestionParser#list_prefix.
    def enterList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#list_prefix.
    def exitList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass

    # Enter a parse tree produced by QuestionParser#list_answer_item.
    def enterList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        from api_v2.models import Answer
        new_answer = Answer()
        self.answer = new_answer
        self.answer.question = self.question
        self.answer.is_correct = True
        self.current_answer_order += 1
        self.answer.order = self.current_answer_order
        self.answer.save()
        self.question.correct_answers_length += 1
        self.question.save()
        pass

    # Exit a parse tree produced by QuestionParser#list_answer_item.
    def exitList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        prefix = self.trim_text(ctx.answer_prefix().getText())
        self.answer.prefix = prefix
        
        answer_text = ""
        for answer_content in ctx.content():
            answer_text += answer_content.getText()
        answer_body = self.markdown_to_html(answer_text)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body
        
        # print("\n--------------------------LIST ANSWER ITEM-------------------------------")
        # print(answer_body)

        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            answer_feedback = ctx.feedback().getText().lstrip()[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        
        self.answer.save()
        pass

    # Enter a parse tree produced by QuestionParser#answer_prefix.
    def enterAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#answer_prefix.
    def exitAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass

 # Enter a parse tree produced by QuestionParser#end_answers.
    def enterEnd_answers(self, ctx:QuestionParser.End_answersContext):
        pass

    # Exit a parse tree produced by QuestionParser#end_answers.
    def exitEnd_answers(self, ctx:QuestionParser.End_answersContext):
        if len(self.questions) == len(ctx.end_answers_item()) :
            self.end_answers = []
            # print("\n--------------------------END ANSWERS-------------------------------")
            for idx, ctx_end_answers_item in enumerate(ctx.end_answers_item()):
                answer = {}
                answer_content = ""
                for ctx_answer_content in ctx_end_answers_item.content():
                    answer_content += ctx_answer_content.getText()

                answer_content = self.trim_text(answer_content)
                # print(answer_content)
                answer['answer'] = answer_content
                answer['feedback'] = None
                
                try:
                    feedback_content = ""
                    for ctx_feedback_content in ctx_end_answers_item.feedback().content():
                        feedback_content += ctx_feedback_content.getText()

                    feedback_content = self.trim_text(feedback_content)
                    answer['feedback'] = feedback_content
                except:
                    # NO FEEDBACK
                    pass

                self.end_answers.append(answer)
        else:
            logger = logging.getLogger('api_v2.QuestionParserListener.exitEnd_answers')
            error_message = f"\n301, Total number of questions doesn't match total answer key. \
                              \n\t Total Questions  : {len(self.questions)} \
                              \n\t Total Answer Key : {len(ctx.end_answers_item())}"
            logger.error(error_message)
        pass

    # Enter a parse tree produced by QuestionParser#end_answers_item.
    def enterEnd_answers_item(self, ctx:QuestionParser.End_answers_itemContext):
        pass

    # Exit a parse tree produced by QuestionParser#end_answers_item.
    def exitEnd_answers_item(self, ctx:QuestionParser.End_answers_itemContext):
        pass

    # Enter a parse tree produced by QuestionParser#question_prefix.
    def enterQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_prefix.
    def exitQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
        pass
    
    def trim_text(self, txt):
        text = txt.strip()
        text = re.sub(' +', ' ', text)
        return text

    def markdown_to_plain(self, text):
        plain_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji", to="plain", extra_args=['--wrap=none'])
        return plain_text

    def markdown_to_html(self, text):
        html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks", to="html", extra_args=["--mathml", '--ascii'])
        return html_text

    def html_to_plain(self, text):
        html_text = pypandoc.convert_text(text, format='html', to="plain", extra_args=['--wrap=none'])
        return html_text

    def process_question(self, question):
        logger = logging.getLogger('api_v2.QuestionParserListener.process_question')
        if question.question_type != None:
            if question.question_type == 'MC':
                if self.is_multiple_choice(question) == True:
                    # BUILD MC
                    pass
                else:
                    error_message = f"\n302, Question {question.prefix} format doesn't match Multiple Choice type format. \
                                      \n\t Right answer allowed : 1 \
                                      \n\t Right answer found   : {question.correct_answers_length}"
                    logger.error(error_message)


            elif question.question_type == 'TF':
                if self.is_true_false(question) == True:
                    # BUILD TF
                    pass
                else:
                    answers_length = len(question.get_answers())
                    is_true_exist = False
                    is_false_exist = False
                    if answers_length == 2:
                        for answer in question.get_answers():
                            text_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                            if "true" == text_answer:
                                is_true_exist = True
                            elif "false" == text_answer:
                                is_false_exist = True

                    error_message = f"\n302, Question {question.prefix} format doesn't match True/False type format."
                    if answers_length != 2:
                        error_message += "\n\t There must be two answer items."
                    
                    if is_true_exist == False:
                        error_message += "\n\t One of the answer item must only consist of the word 'True'."
                    if is_false_exist == False:
                        error_message += "\n\t One of the answer item must only consist of the word 'False'."
                    logger.error(error_message)


            elif question.question_type == 'MS':
                if self.is_multi_select(question) == True:
                    # BUILD MS
                    pass
                else:
                    answers_length = len(question.get_answers())
                    error_message = f"\n302, Question {question.prefix} format doesn't match Multi-Select type format. \
                                      \n\t Minimum answer item needed : 1 \
                                      \n\t Answer item found          : {answers_length}"
                    logger.error(error_message)



            elif question.question_type == 'MT':
                if self.is_matching(question) == True:
                    # BUILD MT
                    pass
                else:
                    count_equal_sign = 0
                    is_one_equal_sign = True
                    if len(question.get_answers()) > 1:
                        for answer in question.get_answers():
                            if "=" in answer.answer_body:
                                count_equal_sign = count_equal_sign + 1
                                if answer.answer_body.count("=") > 1:
                                    is_one_equal_sign = False
                    error_message = f"\n302, Question {question.prefix} format doesn't match Matching type format."
                    if count_equal_sign < len(question.get_answers()):
                        missing_count = len(question.get_answers()) - count_equal_sign
                        error_message += f"\n\t Answer list is missing {missing_count} '=' separator."
                    if is_one_equal_sign == False:
                        error_message += "\n\t More than one '=' separator was found on the answer list."
                    logger.error(error_message)


            elif question.question_type == 'ORD':
                if self.is_ordering(question) == True:
                    # BUILD ORD
                    pass
                else:
                    answers_length = len(question.get_answers())
                    error_message = f"\n302, Question {question.prefix} format doesn't match Ordering type format."
                    if answers_length <=1:
                        error_message += f"\n\t Minimum answer item needed : 2 \
                                           \n\t Answer item found          : {answers_length}"
                    if question.correct_answers_length != None:
                         error_message += "\n\t Answer item shouldn't start with a '*' symbol."
                    logger.error(error_message)


            elif question.question_type == 'FIB':
                if self.is_fill_in_the_blanks(question) == True:
                    # BUILD FIB
                    pass
                else:
                    question_fib_length = len(re.findall(r"\[(.*?)\]", question.question_body))
                    answers_length = len(question.get_fib_answers())
                    error_message = f"\n302, Question {question.prefix} format doesn't match Fill In the Blanks type format."
                    if question_fib_length != answers_length:
                        error_message = "\n\tPlease check your question format or email us at courseproduction@bcit.ca."
                    logger.error(error_message)
                pass


            elif question.question_type == 'WR':
                # TRUST USER & BUILD WR
                pass
            else:
                error_message = f"\n304, Question {question.prefix} doesn't match any type of questions."
                logger.error(error_message)
                pass
        else:
            is_TF = self.is_true_false(question)
            is_MC = self.is_multiple_choice(question)
            is_MS = self.is_multi_select(question)
            is_MT = self.is_matching(question)
            is_ORD = self.is_ordering(question)
            is_WR = self.is_written_response(question)
            is_FIB = self.is_fill_in_the_blanks(question)

            # print('is_TF  :', is_TF)
            # print('is_MC  :', is_MC)
            # print('is_MS  :', is_MS)
            # print('is_MT  :', is_MT)
            # print('is_ORD :', is_ORD)
            # print('is_WR  :', is_WR)
            # print('is_FIB :', is_FIB )

            if is_TF == True:
                question.question_type = "TF"
                question.randomize_answer = False
            elif is_MC == True:
                question.question_type = "MC"
            elif is_MT == True:
                question.question_type = "MT"
                question.randomize_answer = True
            elif is_ORD == True:
                question.question_type = "ORD"
                question.randomize_answer = True
            elif is_MS == True:
                question.question_type = "MS"
            elif is_FIB == True:
                question.question_type = "FIB"
                question.randomize_answer = False
            elif is_WR == True:
                question.question_type = "WR"
                question.randomize_answer = False
            else:
                error_message = f"\n303, Type {question.question_type} doesn't exist for Question {question.prefix}."
                logger.error(error_message)
            question.save()

    def is_multiple_choice(self, question):
        if question.correct_answers_length == 1:
            return True
        return False
    
    def is_true_false(self, question):
        if question.correct_answers_length == 1:
            if len(question.get_answers()) == 2:
                is_true_exist = False
                is_false_exist = False

                for answer in question.get_answers():
                    text_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                    if "true" == text_answer:
                        is_true_exist = True
                    elif "false" == text_answer:
                        is_false_exist = True
                
                if is_true_exist == True:
                    if is_false_exist == True:
                        for answer in question.get_answers():
                            current_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                            if "true" == current_answer:
                                answer.answer_body = "<p>True</p>"
                            elif "false" == current_answer:
                                answer.answer_body = "<p>False</p>"
                            answer.save()
                        return True
        return False

    def is_multi_select(self, question):
        if len(question.get_answers()) > 1:
            return True
        return False

    def is_matching(self, question):
        count_equal_sign = 0
        if len(question.get_answers()) > 1:
            for answer in question.get_answers():
                if "=" in answer.answer_body:
                    count_equal_sign = count_equal_sign + 1
            if(len(question.get_answers()) == count_equal_sign):
                for answer in question.get_answers():
                    split_answer = answer.answer_body.split('=')
                    if len(split_answer) > 2:
                        return False
                    answer.match_left = split_answer[0] + '</p>'
                    answer.match_right = '<p>' + split_answer[1]
                    answer.save()
                return True
        return False

    def is_ordering(self, question):
        if len(question.get_answers()) > 1:
            if question.correct_answers_length == None:
                return True
        return False 

    def is_written_response(self, question):
        if len(question.get_answers()) == 1:
            if question.correct_answers_length == None:
                return True
        return False

    def is_fill_in_the_blanks(self, question):
        if len(question.get_answers()) == 0:
            if question.correct_answers_length == 0:
                if len(question.get_fib_answers()) > 0:
                    question_text = question.question_body
                    wrapped_question_text = re.search(r"^\<p\>(.*?)\<\/p\>$", question.question_body)
                    try:
                        if wrapped_question_text[1]:
                            question_text = wrapped_question_text[1]
                    except:
                        # not wrapped
                        pass
                    question_fib_length = len(re.findall(r"\[(.*?)\]", question_text))
                    if question_fib_length == len(question.get_fib_answers()):
                        fib_order = 0
                        for index, fib_answer in enumerate(question.get_fib_answers()):
                            regex_pattern = r"\[\s?(" + re.escape(fib_answer.text) + ")\s?\]"
                            blank = re.search(regex_pattern, question_text)
                            if blank.group(1) != None:
                                reg = re.compile('(.+)'+ re.escape(blank.group(0)))
                                fib_question_text = reg.search(question_text).group(1)
                                trimmed_text = self.trim_text(self.html_to_plain(fib_question_text))
                                if len(trimmed_text) > 0:
                                    fib_order += 1
                                    from api_v2.models import Fib
                                    new_fib = Fib()
                                    fib = new_fib
                                    fib.question = question
                                    fib.type = "question"
                                    fib.text = fib_question_text
                                    fib.order = fib_order
                                    fib.save()
                                fib_order += 1
                                fib_answer.order = fib_order
                                fib_answer.save()
                                regex_pattern_2 = r".*\[\s?(" + re.escape(fib_answer.text) + ")\s?\]"
                                question_text = re.sub(regex_pattern_2, "", question_text, 1)
                                re_question_body = re.sub(regex_pattern, "_______", question.question_body, 1)
                                question.question_body = re_question_body
                                question.title = self.html_to_plain(re_question_body)
                                question.save()
                                if(len(question.get_fib_answers()) == index+1):
                                    trimmed_text = self.trim_text(self.html_to_plain(question_text))
                                    if len(trimmed_text) > 0:
                                        fib_order += 1

                                        from api_v2.models import Fib
                                        new_fib = Fib()

                                        fib = new_fib
                                        fib.question = question
                                        fib.type = "question"
                                        fib.text = question_text
                                        fib.order = fib_order
                                        fib.save()

                                    return True
                            
                return False
                pass

del QuestionParser