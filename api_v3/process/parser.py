import os
# import subprocess
# import re
import xml.etree.ElementTree as ET
from ..models import EndAnswer, Section, Question
# from .process_helper import trim_text, markdown_to_plain, trim_md_to_html
# from .questionbuilder.truefalse import build_inline_TF, build_endanswer_TF
# from .questionbuilder.multiplechoice import build_inline_MC, build_endanswer_MC
# from .questionbuilder.multipleselect import build_inline_MS, build_endanswer_MS
# from .questionbuilder.fib import build_inline_FIB, build_endanswer_FIB
# from .questionbuilder.matching import build_inline_MAT, build_endanswer_MAT
# from .questionbuilder.ordering import build_inline_ORD, build_endanswer_ORD
# from .questionbuilder.writtenresponse import build_inline_WR_with_keyword, build_inline_WR_with_list, build_endanswer_WR_with_list

from django.conf import settings
import logging
logger = logging.getLogger(__name__)
from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter
# import threading
# from asgiref.sync import sync_to_async
# import time
# import asyncio
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from api_v3.tasks import parse_question

from celery import group

def run_parser(questionlibrary):
    loggingfilter = QuestionlibraryFilenameFilter(questionlibrary=questionlibrary)
    logger.addFilter(loggingfilter)
    import time
    sections = Section.objects.filter(question_library=questionlibrary)
    if len(sections) == 0:
        raise ParserError("No sections found for the parser to work on")
    endanswers = EndAnswer.objects.filter(question_library=questionlibrary)    
    question_count = 0
    section_count = 0
    start_time = time.time()
    for section in sections:
        questions = Question.objects.filter(section=section)
        if section.is_main_content:
            logger.debug("Root section:")
        else:
            section_count += 1
            logger.debug("Section", str(section.order), ":", section.title )

        section.questions_expected = len(questions) - 1
        section_start_time = time.time()
        section_question_count = 0

        # ----------------------- DELETE empty questions before adding to thread

        for question in questions:
            # discard empty question
            if question.raw_content is None:
                question.delete()

# ========THREADS 
        # ----------------------- ADD questionparser to thread here 
        # threads = []
        # for idx, question in enumerate(questions):
        #     if len(endanswers) != 0:
        #         t = threading.Thread(target=parse_question, args=[questionlibrary, question, endanswers[idx]], daemon=True)
        #         threads.append(t)
        #     else:
        #         t = threading.Thread(target=parse_question, args=[questionlibrary, question, None], daemon=True)
        #         threads.append(t)
        #     section_question_count += 1
        #     if settings.DEBUG:
        #         print("    question : " + str(question_count + section_question_count))
        # # ----------------------- START threads here
        # for x in threads:
        #     x.start()    
        # # ----------------------- WAIT for all threads to finish
        # for x in threads:
        #     x.join()
        
# ======== NO THREADS
        # for idx, question in enumerate(questions):
        #     # discard empty question
        #     if question.raw_content is None:
        #         question.delete()
        #     else:
        #         if len(endanswers) != 0:
        #             parse_question(questionlibrary, question, endanswers[idx])
        #         else:
        #             parse_question(questionlibrary, question)            
        #     section_question_count += 1
        #     if settings.DEBUG:
        #         print("    question : " + str(question_count + section_question_count))

        try:
            questions = Question.objects.filter(section=section)
            tasklist = []
            for idx, question in enumerate(questions):
                if len(endanswers) != 0:
                    tasklist.append(parse_question.s(questionlibrary.randomize_answer, question.id, endanswers[idx].id))
                else:
                    tasklist.append(parse_question.s(questionlibrary.randomize_answer, question.id))
                section_question_count += 1
            lazy_group = group(tasklist)
            promise = lazy_group()
            promise.get()
        except:
            raise ParserError("Error in Parser group task")

        question_count += section_question_count
        section_end_time = time.time()
        section.processing_time = section_end_time - section_start_time
        section.save()
        logger.debug(f"  Section total questions : {section_question_count}")
        logger.debug(f"  Section processing time : {section.processing_time}")
    logger.info(f'Total Processing time for Parser : {time.time() - start_time}')
    logger.debug(f"Processing Time Total :  {time.time() - start_time}")

class ParserError(Exception):
    def __init__(self, reason, message="Parser Error"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'