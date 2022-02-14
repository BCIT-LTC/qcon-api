# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .serializers import WordToJsonSerializer
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


# class WordToZip(APIView):
#     parser_classes = [MultiPartParser]
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthenticationWithBearer]
#     serializer_class = WordToZipSerializer

#     @extend_schema(
#         # override default docstring extraction
#         description=
#         'Upload a Word document(.docx) and receive a zip(.zip) file',
#         # provide Authentication class that deviates from the views default
#         auth=None,
#         # change the auto-generated operation name
#         operation_id=None,
#         # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
#         operation=None,
#         # attach request/response examples to the operation.
#     )
#     def post(self, request, format=None):
#         # file_obj = request.FILES.get('temp_file')
#         is_random = False
#         if 'randomize' in request.POST:
#             if request.POST['randomize'].lower() in ("true", "yes"):
#                 is_random = True

#         file_obj2 = request.data['temp_file']
#         serializer = WordToZipSerializer(data={
#             'temp_file': file_obj2,
#             'randomize': is_random
#         })

#         if serializer.is_valid():
#             instance = serializer.save()

#             filename = instance.zip_file.name.split("/")[1]

#             if (instance.total_question_errors +
#                     instance.total_document_errors == 0):
#                 theresponse = FileResponse(instance.zip_file)
#                 theresponse[
#                     'Content-Disposition'] = 'attachment; filename="' + filename + '"'
#                 logger.info("[" + str(instance.transaction) + "] " +
#                             ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
#                 instance.cleanup()
#                 return theresponse
#             else:
#                 #Serializer to query only the records that contain errors

#                 serialized_data = QuestionLibraryErrorSummarySerializer(
#                     instance)

#                 logger.info(
#                     "[" + str(instance.transaction) + "] " +
#                     ">>>>>>>>>>Transaction Finished with errors>>>>>>>>>>")

#                 theresponse = JsonResponse(serialized_data.data, status=201)
#                 instance.cleanup()
#                 return theresponse

#         return JsonResponse(serializer.errors, status=400)

# class WordToJsonZip(APIView):
#     parser_classes = [MultiPartParser]
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthenticationWithBearer]
#     serializer_class = WordToJsonZipSerializer

#     @extend_schema(
#         # override default docstring extraction
#         description=
#         'Upload a Word document(.docx) and receive a Zip package with Json included',
#         # provide Authentication class that deviates from the views default
#         auth=None,
#         # change the auto-generated operation name
#         operation_id=None,
#         # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
#         operation=None,
#         # attach request/response examples to the operation.
#     )
#     def post(self, request, format=None):
#         # file_obj = request.FILES.get('temp_file')
#         file_obj2 = request.data['temp_file']

#         is_random = False
#         if 'randomize' in request.POST:
#             if request.POST['randomize'].lower() in ("true", "yes"):
#                 is_random = True

#         convertserializer = WordToJsonZipSerializer(data={
#             'temp_file': file_obj2,
#             'randomize': is_random
#         })

#         if convertserializer.is_valid():
#             instance = convertserializer.save()

#             question_library = QuestionLibrary.objects.get(
#                 transaction=instance.transaction.id)

#             question_library_serializer = QuestionLibrarySerializer(
#                 question_library)
#             import json
#             # print(json.dumps(question_library_serializer.data, indent=4))
#             jsonfile = ContentFile(str(
#                 json.dumps(question_library_serializer.data, indent=4)),
#                                    name="output.json")
#             instance.json_file = jsonfile
#             instance.save()
#             if instance.total_document_errors == 0:
#                 instance.create_zip_file_package()

#                 filename = instance.output_zip_file.name.split("/")[1]
#                 file_response = FileResponse(instance.output_zip_file)
#                 file_response[
#                     'Content-Disposition'] = 'attachment; filename="' + filename + '"'

#                 logger.info("[" + str(instance.transaction) + "] " +
#                             ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
#                 instance.cleanup()
#                 return file_response
#             else:
#                 #Query only the records that contain errors
#                 serialized_data = QuestionLibraryErrorSummarySerializer(
#                     instance)
#                 theresponse = JsonResponse(serialized_data.data, status=400)

#                 logger.info(
#                     "[" + str(instance.transaction) + "] " +
#                     ">>>>>>>>>>Transaction Finished with document error>>>>>>>>>>"
#                 )
#                 instance.cleanup()
#                 return theresponse

#             # return Response("None")
#         return JsonResponse(convertserializer.errors, status=400)


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
        # file_obj = request.FILES.get('temp_file')
        file_obj2 = request.data['temp_file']
        serializer = WordToJsonSerializer(data={'temp_file': file_obj2})

        if serializer.is_valid():
            instance = serializer.save()

            # question_library = QuestionLibrary.objects.get(
            #     transaction=instance.transaction.id)

            # question_library = instance

            # ==============  start the process  ========
            from .process import process
            process(instance)

            # question_library_serializer = QuestionLibrarySerializer(
            #     question_library)

            
            json_test = { "section_name": "ABC", "randomize_answer": "null", "total_question_errors": "0", "total_document_errors": "0", "documenterrors": [], "questions": [ { "prefix": "1", "title": "is a measure of:", "points": "1.0", "randomize_answer": "null", "question_type": "MC", "question_body": "<p>is a measure of:</p>", "question_feedback": "null", "hint": "null", "correct_answers_length": 1, "questionerrors": [], "answers": [ { "prefix": "a.", "answer_body": "<p>Resistance</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 1 }, { "prefix": "b.", "answer_body": "<p>Current</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 2 }, { "prefix": "c.", "answer_body": "<p>Impedance</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 3 }, { "prefix": "d. \\*", "answer_body": "<p>Voltage</p>", "answer_feedback": "null", "is_correct": "true", "match_left": "null", "match_right": "null", "order": 4 } ], "fib": [] }, { "prefix": "2", "title": "Amplitude (2) of:", "points": "1.0", "randomize_answer": "null", "question_type": "MC", "question_body": "<p><em>Amplitude</em> (2) of:</p>", "question_feedback": "null", "hint": "null", "correct_answers_length": 1, "questionerrors": [], "answers": [ { "prefix": "a.", "answer_body": "<p>aaa</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 1 }, { "prefix": "b.", "answer_body": "<p>bbb</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 2 }, { "prefix": "c.", "answer_body": "<p>xxx</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 3 }, { "prefix": "d. \\*", "answer_body": "<p>sss</p>", "answer_feedback": "null", "is_correct": "true", "match_left": "null", "match_right": "null", "order": 4 } ], "fib": [] }, { "prefix": "3", "title": "of:", "points": "1.0", "randomize_answer": "null", "question_type": "MC", "question_body": "<p>of:</p>", "question_feedback": "null", "hint": "null", "correct_answers_length": 1, "questionerrors": [], "answers": [ { "prefix": "a.", "answer_body": "<p>Resistance</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 1 }, { "prefix": "b.", "answer_body": "<p>Current</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 2 }, { "prefix": "c.", "answer_body": "<p>Impedance</p>", "answer_feedback": "null", "is_correct": "false", "match_left": "null", "match_right": "null", "order": 3 }, { "prefix": "d. \\*", "answer_body": "<p>Voltage</p>", "answer_feedback": "null", "is_correct": "true", "match_left": "null", "match_right": "null", "order": 4 } ], "fib": [] } ] }
            json_string = str(json.dumps(json_test, indent=4))
            json_file = ContentFile(json_string, name="result.json")
            instance.json_file = json_file
            instance.save()
            file_response = FileResponse(instance.json_file)
            file_response['Content-Disposition'] = 'attachment; filename="' + "result.json" + '"'

            instance.cleanup()
            return file_response

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