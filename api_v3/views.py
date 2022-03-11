# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .serializers import JsonToScormSerializer, QuestionLibraryErrorSummarySerializer, QuestionLibrarySerializer, WordToJsonSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser

from django.core.files.base import ContentFile
from django.conf import settings

from .models import QuestionLibrary

import logging
logger = logging.getLogger(__name__)


class TokenAuthenticationWithBearer(TokenAuthentication):
    keyword = 'Bearer'

    def __init__(self):
        super(TokenAuthenticationWithBearer, self).__init__()

class WordToJson(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthenticationWithBearer]
    serializer_class = WordToJsonSerializer

    @extend_schema(
        # override default docstring extraction
        description='Upload a Word document(.docx) and return a JSON file (.json)',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def post(self, request, format=None):

        is_random = False
        if 'randomize' in request.POST:
            if request.POST['randomize'].lower() in ("true", "yes"):
                is_random = True

        file_obj = request.data['temp_file']
        serializer = WordToJsonSerializer(data={
            'temp_file': file_obj,
            'randomize': is_random
        })

        if serializer.is_valid():
            instance = serializer.save()

            # question_library = QuestionLibrary.objects.first()

            # question_library = instance

            # ==============  start the process  ========
            from .process import process
            process(instance)

            # question_library_serializer = QuestionLibrarySerializer(question_library)

            
            json_test = {"general_header": "General Header","randomize_answer":False,"total_question_errors": "1","total_document_errors": "0","sections": [{"title": "Section title","is_title_displayed":False,"text":None,"is_text_displayed":False,"shuffle":False,"questions": [{"title": "MC title","text": "Question text","point": 3.5,"difficulty": 3,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice": {"randomize":True,"enumeration": 1,"multiple_choices_answers": [{"answer": "MC first answer text","answer_feedback": "MC first answer feedback","weight": 100},{"answer": "MC second answer text","answer_feedback": "MC second answer feedback","weight": 0}]},"true_false":None,"fib":None,"multiple_select":None,"written_response":None},{"title": "TF title","text": "Question text","point": 1,"difficulty": 1,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false": {"true_weight": 100,"true_feedback": "True feedback","false_weight": 0,"false_feedback": "True feedback","enumeration": 2},"fib":None,"multiple_select":None,"written_response":None},{"title": "MS title","text": "Question text","point": 1,"difficulty": 1,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib":None,"multiple_select": {"randomize":True,"enumeration": 1,"style": 2,"multiple_select_answers": [{"answer": "MS first answer text","answer_feedback": "MS first answer feedback","is_correct":True},{"answer": "MS second answer text","answer_feedback": "MS second answer feedback","is_correct":True}]},"written_response":None},{"title": "WR title","text": "Question text","point": 5,"difficulty": 5,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib":None,"multiple_select":None,"written_response": {"enable_student_editor":False,"initial_text":None,"answer_key": "WR answer key","enable_attachments":False}},{"title": "FIB title","text": "Question text","point": 4,"difficulty": 3,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": [{"type": "fibquestion","text": "1+15?","order": 1,"size":None,"weight":None},{"type": "fibanswer","text": "16","order": 2,"size": 3,"weight": 100}],"multiple_select":None,"written_response":None},{"title": "Ordering title","text": "Question text","point": 6,"difficulty": 2,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": None,"multiple_select":None,"ordering": [{"text": "Order 1","order": 1,"ord_feedback": "Ordering 1 feedback"},{"text": "Order 1","order": 2,"ord_feedback": "Ordering 2 feedback"},{"text": "Order 1","order": 3,"ord_feedback": "Ordering 3 feedback"}],"matching":None,"written_response":None},{"title": "Matching title","text": "Question text","point": 6,"difficulty": 2,"mandatory":False,"hint": "Question hint","feedback": "Question feedback","multiple_choice":None,"true_false":None,"fib": None,"multiple_select":None,"ordering": None,"matching": {"grading_type": 1,"matching_choices": [{"choice_text": "Choice 1","matching_answers": [{"answer_text": "Choice 1 answer a"},{"answer_text": "Choice 1 answer b"}]},{"choice_text": "Choice 2","matching_answers": [{"answer_text": "Choice 2 answer a"},{"answer_text": "Choice 2 answer b"}]}]},"written_response":None}]}]}
            # json_string = str(json.dumps(json_test, indent=4))
            for item in json_test:
                match item:
                    case "general_header":
                        print(json_test["general_header"])
                    case "randomize_answer":
                        print(json_test["randomize_answer"])
                    case "total_question_errors":
                        print(json_test["total_question_errors"])
                    case "total_document_errors":
                        print(json_test["total_document_errors"])
                    case "sections":
                        for section in json_test["sections"]:
                            print("\t", section["title"])
                            print("\t", section["is_title_displayed"])
                            print("\t", section["text"])
                            print("\t", section["is_text_displayed"])
                            print("\t", section["shuffle"])

                            for question in section["questions"]:
                                print("\t\t", question["title"])
                                print("\t\t", question["text"])
                                print("\t\t", question["point"])
                                print("\t\t", question["difficulty"])
                                print("\t\t", question["mandatory"])
                                print("\t\t", question["hint"])
                                print("\t\t", question["feedback"])
                                
                                if question["multiple_choice"]:
                                    print("\t\t\tmultiple_choice")
                                    print("\t\t\t\t", question["multiple_choice"]["randomize"])
                                    print("\t\t\t\t", question["multiple_choice"]["enumeration"])

                                    print("\t\t\t\tmultiple_choices_answers")
                                    for mc_answers in question["multiple_choice"]["multiple_choices_answers"]:
                                        print("\t\t\t\t\t", mc_answers["answer"])
                                        print("\t\t\t\t\t", mc_answers["answer_feedback"])
                                        print("\t\t\t\t\t", mc_answers["weight"])
                                        print("")
                                                    
                                elif question["true_false"] :
                                    print("\t\t\ttrue_false")
                                    print("\t\t\t\t", question["true_false"]["true_weight"])
                                    print("\t\t\t\t", question["true_false"]["true_feedback"])
                                    print("\t\t\t\t", question["true_false"]["false_weight"])
                                    print("\t\t\t\t", question["true_false"]["false_feedback"])
                                    print("\t\t\t\t", question["true_false"]["enumeration"])

                                elif question["fib"] :
                                    print("\t\t\tfib")
                                    for fib in question["fib"]:
                                        print("\t\t\t\t", fib["type"])
                                        print("\t\t\t\t", fib["text"])
                                        print("\t\t\t\t", fib["order"])
                                        print("\t\t\t\t", fib["size"])
                                        print("\t\t\t\t", fib["weight"])
                                        print("")
                                elif question["multiple_select"]:
                                    print("\t\t\tmultiple_select")
                                    print("\t\t\t\t", question["multiple_select"]["randomize"])
                                    print("\t\t\t\t", question["multiple_select"]["enumeration"])
                                    print("\t\t\t\t", question["multiple_select"]["style"])

                                    print("\t\t\t\tmultiple_select_answers")
                                    for ms_answers in question["multiple_select"]["multiple_select_answers"]:
                                        print("\t\t\t\t\t", ms_answers["answer"])
                                        print("\t\t\t\t\t", ms_answers["answer_feedback"])
                                        print("\t\t\t\t\t", ms_answers["is_correct"])
                                        print("")

                                elif question["written_response"]:
                                    print("\t\t\twritten_response")
                                    print("\t\t\t\t", question["written_response"]["enable_student_editor"])
                                    print("\t\t\t\t", question["written_response"]["initial_text"])
                                    print("\t\t\t\t", question["written_response"]["answer_key"])
                                    print("\t\t\t\t", question["written_response"]["enable_attachments"])

                                elif question["matching"]:
                                    print("\t\t\tmatching")
                                    print("\t\t\t\t", question["matching"]["grading_type"])

                                    print("\t\t\t\tmatching_choices")
                                    for matching_choice in question["matching"]["matching_choices"]:
                                        print("\t\t\t\t\t", matching_choice["choice_text"])
                                        if matching_choice["matching_answers"]:
                                            for matching_answer in matching_choice["matching_answers"]:
                                                print("\t\t\t\t\t\t", matching_answer["answer_text"])
                                                print("")
                                
                                elif question["ordering"]:
                                    print("\t\t\tordering")
                                    for ordering in question["ordering"]:
                                        print("\t\t\t\t", ordering["text"])
                                        print("\t\t\t\t", ordering["order"])
                                        print("\t\t\t\t", ordering["ord_feedback"])
                                        print("")
                                else:
                                    print("******************************************************")
                                    print("NO QUESTION TYPE\n\n")
                                    print(question)
                                    print("******************************************************")



               


            instance.json_output = json_test
            instance.save()
            # print(instance.json_output)
            instance.cleanup()
            return JsonResponse(json_test, status=200)

        return JsonResponse(serializer.errors, status=400)


class JsonToScorm(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthenticationWithBearer]
    serializer_class = JsonToScormSerializer

    @extend_schema(
        # override default docstring extraction
        description=
        'Upload a JSON file(.json) and receive a SCORM (.zip) file',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def post(self, request, format=None):
        is_random = False
        if 'randomize' in request.POST:
            if request.POST['randomize'].lower() in ("true", "yes"):
                is_random = True

        file_obj = request.data['temp_file']
        serializer = JsonToScormSerializer(data={
            'temp_file': file_obj,
            'randomize': is_random
        })

        if serializer.is_valid():
            instance = serializer.save()

            # file_name = instance.zip_file.name.split("/")[1]
            file_name = 'insert_zip_file_name_here'

            if (instance.total_question_errors +
                    instance.total_document_errors == 0):
                file_response = FileResponse(instance.zip_file)
                file_response[
                    'Content-Disposition'] = 'attachment; filename="' + file_name + '"'
                logger.info("[" + str(instance.id) + "] " +
                            ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
                instance.cleanup()
                return file_response
            else:
                #Serializer to query only the records that contain errors

                serialized_data = QuestionLibraryErrorSummarySerializer(
                    instance)

                logger.info(
                    "[" + str(instance.id) + "] " +
                    ">>>>>>>>>>Transaction Finished with errors>>>>>>>>>>")

                json_response = JsonResponse(serialized_data.data, status=201)
                instance.cleanup()
                return json_response

        return JsonResponse(serializer.errors, status=400)


class RootPath(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        from .models import StatusResponse
        from .serializers import StatusResponseSerializer

        status = StatusResponse(name='qcon-api',
                                app_description=settings.APP_DESCRIPTION,
                                version_number=settings.GIT_TAG,
                                build_hash=settings.BUILD_HASH,
                                build_short_sha=settings.BUILD_SHORT_SHA,
                                build_date=settings.BUILD_DATE,
                                cluster_name=settings.CLUSTER_NAME,
                                build_env=settings.BUILD_ENV,
                                app_tagline=settings.APP_TAGLINE)
        serializer = StatusResponseSerializer(status)

        return JsonResponse(serializer.data,
                            json_dumps_params={'indent': 2},
                            status=200)


from django.shortcuts import redirect


def view_404(request, exception=None):
    return redirect('/')


def redirect_view(request, namespace, name, slug, actualurl):
    print(slug)
    print(actualurl)
    return redirect('/' + actualurl)
    # return None


def redirect_root(request, namespace, name, slug):
    print(slug)
    return redirect('/')