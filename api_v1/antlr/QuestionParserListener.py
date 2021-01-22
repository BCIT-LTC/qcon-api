# Generated from QuestionParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuestionParser import QuestionParser
else:
    from QuestionParser import QuestionParser
import re
import pypandoc
from api_v1.models import Question, Answer, Fib
from datetime import datetime

# This class defines a complete listener for a parse tree produced by QuestionParser.
class QuestionParserListener(ParseTreeListener):
    def __init__(self, question_library):
        self.questions = []
        self.question = None
        self.answers = []
        self.answer = None
        self.question_library = question_library
        self.end_answers = None

    # Return parsed question
    def get_results(self):
        return self.questions

    # Enter a parse tree produced by QuestionParser#parse_question.
    def enterParse_question(self, ctx:QuestionParser.Parse_questionContext):
        self.question = Question()
        self.question.question_library = self.question_library
        self.question.save()
        pass

    # Exit a parse tree produced by QuestionParser#parse_question.
    def exitParse_question(self, ctx:QuestionParser.Parse_questionContext):
        print('')
        if self.end_answers == None:
            for question_index, question in enumerate(self.questions):
                self.process_question(question)
                self.question.save()
                print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
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
                    # either MT or WR
                    is_wr = False
                    fib_answers = question.get_fib_answers()
                    if len(fib_answers) > 0: 
                        if ';' in end_answer:
                            # Multi FIB
                            end_answers_split = end_answer.split(";")
                            for answer_index, answer_text in enumerate(end_answers_split):
                                fib_answer = fib_answers[answer_index]
                                fib_answer.type = "answer"
                                fib_answer.text = answer_text
                                fib_answer.save()
                        else:
                            # only one FIB
                            fib_answer = question.get_fib_answers()[0]
                            fib_answer.type = "answer"
                            fib_answer.text = end_answer
                            fib_answer.save()
                    elif ';' in end_answer:
                        end_answers_split = end_answer.split(";")
                        
                        count_matching = 0
                        for answer_text in end_answers_split:
                            if '=' in answer_text:
                                count_matching = count_matching + 1

                        if count_matching == len(end_answers_split):
                            # MT
                            question.question_type = 'MT'
                            question.save()
                            for answer_text in end_answers_split:
                                matching_answer = Answer()
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
                        question.save()
                        wr_answer = Answer()
                        wr_answer.question = question
                        wr_answer.answer_body = end_answer
                        wr_answer.save()
                            
                self.process_question(question)
                self.question.save()
                print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
        print('')
        pass

    # Enter a parse tree produced by QuestionParser#question.
    def enterQuestion(self, ctx:QuestionParser.QuestionContext):
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
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeOrd.
    def enterTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOrd.
    def exitTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        self.question.question_type = 'ORD'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeFib.
    def enterTypeFib(self, ctx:QuestionParser.TypeFibContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeFib.
    def exitTypeFib(self, ctx:QuestionParser.TypeFibContext):
        self.question.question_type = 'FIB'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeWr.
    def enterTypeWr(self, ctx:QuestionParser.TypeWrContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeWr.
    def exitTypeWr(self, ctx:QuestionParser.TypeWrContext):
        self.question.question_type = 'WR'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#TypeOther.
    def enterTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOther.
    def exitTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        self.question.question_type = 'OTHER'
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#title.
    def enterTitle(self, ctx:QuestionParser.TitleContext):
        pass

    # Exit a parse tree produced by QuestionParser#title.
    def exitTitle(self, ctx:QuestionParser.TitleContext):
        title = self.trim_text(ctx.title().getText()).split(":")[1]
        title = self.markdown_to_plain(title)
        title = self.trim_text(title)
        self.question.title = title
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#points.
    def enterPoints(self, ctx:QuestionParser.PointsContext):
        pass

    # Exit a parse tree produced by QuestionParser#points.
    def exitPoints(self, ctx:QuestionParser.PointsContext):
        points = self.trim_text(ctx.point().getText()).split(":")[1]
        points = self.markdown_to_plain(points)
        points = self.trim_text(points)
        self.question.points = points
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#RandomTrue.
    def enterRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomTrue.
    def exitRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        self.question.randomize_answer = True
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#RandomFalse.
    def enterRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomFalse.
    def exitRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
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
        print("--------------------------QUESTION-------------------------------")
        question_body = self.markdown_to_html(body_text)
        question_body = self.trim_text(question_body)
        self.question.question_body = question_body
        print(question_body)
        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            question_feedback = ctx.feedback().getText().lstrip()[1:]
            question_feedback = self.markdown_to_html(question_feedback)
            question_feedback = self.trim_text(question_feedback)
            self.question.question_feedback = question_feedback
        
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#question_prefix.
    def enterQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_prefix.
    def exitQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
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
        fib = Fib()
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
        pass

    # Exit a parse tree produced by QuestionParser#ListNoAnswer.
    def exitListNoAnswer(self, ctx:QuestionParser.ListNoAnswerContext):
        self.question.correct_answers_length = None
        self.question.save()
        pass

    # Enter a parse tree produced by QuestionParser#ListWithAnswer.
    def enterListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        pass
    
    # Exit a parse tree produced by QuestionParser#ListWithAnswer.
    def exitListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        pass

    # Enter a parse tree produced by QuestionParser#list_item.
    def enterList_item(self, ctx:QuestionParser.List_itemContext):
        self.answer = Answer()
        self.answer.question = self.question
        self.answer.is_correct = False
        self.answer.save()
        pass

    # Exit a parse tree produced by QuestionParser#list_item.
    def exitList_item(self, ctx:QuestionParser.List_itemContext):
        prefix = self.trim_text(ctx.list_prefix().getText())
        self.answer.prefix = prefix

        answer_text = ""
        for answer_content in ctx.content():
            answer_text += answer_content.getText()
        print("--------------------------LIST ITEM-------------------------------")
        answer_body = self.markdown_to_html(answer_text)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body
        print(answer_body)

        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            answer_feedback = ctx.feedback().getText().lstrip()[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        
        self.answer.save()
        self.answers.append(self.answer)
        pass

    # Enter a parse tree produced by QuestionParser#list_prefix.
    def enterList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#list_prefix.
    def exitList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass

    # Enter a parse tree produced by QuestionParser#list_answer_item.
    def enterList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        self.answer = Answer()
        self.answer.question = self.question
        self.answer.is_correct = True
        self.question.correct_answers_length += 1
        self.answer.save()
        pass

    # Exit a parse tree produced by QuestionParser#list_answer_item.
    def exitList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        prefix = self.trim_text(ctx.answer_prefix().getText())
        self.answer.prefix = prefix
        
        answer_text = ""
        for answer_content in ctx.content():
            answer_text += answer_content.getText()
        print("--------------------------LIST ANSWER ITEM-------------------------------")
        answer_body = self.markdown_to_html(answer_text)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body
        print(answer_body)

        # TODO: Find a better way to parse this in exitFeedback()
        if ctx.feedback() != None:
            answer_feedback = ctx.feedback().getText().lstrip()[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        
        self.answer.save()
        self.answers.append(self.answer)
        pass

    # Enter a parse tree produced by QuestionParser#answer_prefix.
    def enterAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#answer_prefix.
    def exitAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass


    def trim_text(self, txt):
        text = txt.strip()
        text = re.sub(' +', ' ', text)
        return text

    def markdown_to_plain(self, text):
        plain_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji", to="plain").replace('\n', ' ')
        return plain_text

    def markdown_to_html(self, text):
        html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks", to="html", extra_args=["--mathml", '--ascii'])
        return html_text

    def html_to_plain(self, text):
        html_text = pypandoc.convert_text(text, format='html', to="plain")
        return html_text

    def process_question(self, question):
        
        if question.question_type != None:
            if question.question_type == 'MC':
                if self.is_multiple_choice(question) == True:
                    # BUILD MC
                    pass
                else:
                    print("Wrong question Format: MC")
            elif question.question_type == 'TF':
                if self.is_true_false(question) == True:
                    # BUILD TF
                    pass
                else:
                    print("Wrong question Format: TF")
            elif question.question_type == 'MS':
                if self.is_multi_select(question) == True:
                    # BUILD MS
                    pass
                else:
                    print("Wrong question Format: MS")
            elif question.question_type == 'MT':
                if self.is_matching(question) == True:
                    # BUILD MT
                    pass
                else:
                    print("Wrong question Format: MT")
            elif question.question_type == 'ORD':
                if self.is_ordering(question) == True:
                    # BUILD ORD
                    pass
                else:
                    print("Wrong question Format: ORD")
            elif question.question_type == 'FIB':
                # if self.is_fill_in_the_blanks(question) == True:
                # BUILD FIB
                pass
            elif question.question_type == 'WR':
                # TRUST USER & BUILD WR
                pass
            else:
                # TODO LOG WRONG QUESTION FORMAT
                print("UNKNOWN QUESTION FORMAT")
                pass
        else:
            is_TF = self.is_true_false(question)
            is_MC = self.is_multiple_choice(question)
            is_MS = self.is_multi_select(question)
            is_MT = self.is_matching(question)
            is_ORD = self.is_ordering(question)
            is_WR = self.is_written_response(question)
            is_FIB = self.is_fill_in_the_blanks(question)

            print('is_TF :', is_TF)
            print('is_MC :', is_MC)
            print('is_MS :', is_MS)
            print('is_MT :', is_MT)
            print('is_ORD :', is_ORD)
            print('is_WR :', is_WR)
            print('is_FIB :',is_FIB )

            if is_TF == True:
                question.question_type = "TF"
            elif is_MC == True:
                question.question_type = "MC"
            elif is_MT == True:
                question.question_type = "MT"
            elif is_MS == True:
                question.question_type = "MS"
            elif is_ORD == True:
                question.question_type = "ORD"
            elif is_FIB == True:
                question.question_type = "FIB"
            elif is_WR == True:
                question.question_type = "WR"
            question.save()

    def is_multiple_choice(self, question):
        if question.correct_answers_length == 1:
            return True
        return False
    
    def is_true_false(self, question):
        if question.correct_answers_length == 1:
            if len(self.answers) == 2:
                is_true_exist = False
                is_false_exist = False

                for answer in self.answers:
                    text_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                    if "true" == text_answer:
                        is_true_exist = True
                    elif "false" == text_answer:
                        is_false_exist = True
                
                if is_true_exist == True:
                    if is_false_exist == True:
                        for answer in self.answers:
                            current_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                            if "true" == current_answer:
                                answer.answer_body = "True"
                            elif "false" == current_answer:
                                answer.answer_body = "False"
                            answer.save()
                        return True
        return False

    def is_multi_select(self, question):
        if len(self.answers) > 1:
            return True
        return False

    def is_matching(self, question):
        count_equal_sign = 0
        if len(self.answers) >= 1:
            for answer in self.answers:
                if "=" in answer.answer_body:
                    count_equal_sign = count_equal_sign + 1
            if(len(self.answers) == count_equal_sign):
                for answer in self.answers:
                    split_answer = answer.answer_body.split('=')
                    if len(split_answer) > 2:
                        return False
                    answer.match_left = split_answer[0] + '</p>'
                    answer.match_right = '<p>' + split_answer[1]
                    answer.save()
                return True
        return False

    def is_ordering(self, question):
        if len(self.answers) > 1:
            if question.correct_answers_length == 0:
                return True
        return False 

    def is_written_response(self, question):
        if len(self.answers) == 1:
            if question.correct_answers_length == 0:
                return True
        return False

    def is_fill_in_the_blanks(self, question):
        if len(self.answers) == 0:
            if question.correct_answers_length == 0:
                if len(question.get_fib_answers()) > 0:
                    question_text = question.question_body
                    question_fib_length = len(re.findall(r"(?<!!)(?=\[(.*?)\])(?!\()", question_text))
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
                                    fib = Fib()
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
                                question.question_body = re.sub(regex_pattern, "_______", question.question_body, 1)
                                question.save()
                                if(len(question.get_fib_answers()) == index+1):
                                    trimmed_text = self.trim_text(self.html_to_plain(question_text))
                                    if len(trimmed_text) > 0:
                                        fib_order += 1
                                        fib = Fib()
                                        fib.question = question
                                        fib.type = "question"
                                        fib.text = question_text
                                        fib.order = fib_order
                                        fib.save()
                                        return True
                            
                return False
                pass

del QuestionParser