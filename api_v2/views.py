# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .serializers import QuestionLibrarySerializer, WordToZipSerializer, WordToJsonSerializer, WordToJsonZipSerializer, QuestionLibraryErrorSummarySerializer
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
# from os import makedirs, path, walk

from .models import QuestionError, QuestionLibrary
from .models import Question
from .models import Transaction

# from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)
# WordToJsonZip_Logger = logging.getLogger('api_v2.views.WordToJsonZip')

# WordToZip_Logger = logging.getLogger('api_v2.views.WordToZip')


class TokenAuthenticationWithBearer(TokenAuthentication):
    keyword = 'Bearer'

    def __init__(self):
        super(TokenAuthenticationWithBearer, self).__init__()


class WordToZip(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthenticationWithBearer]
    serializer_class = WordToZipSerializer

    @extend_schema(
        # override default docstring extraction
        description=
        'Upload a Word document(.docx) and receive a zip(.zip) file',
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
        is_random = False
        if 'randomize' in request.POST:
            if request.POST['randomize'].lower() in ("true", "yes"):
                is_random = True

        file_obj2 = request.data['temp_file']
        serializer = WordToZipSerializer(data={
            'temp_file': file_obj2,
            'randomize': is_random
        })

        if serializer.is_valid():
            instance = serializer.save()

            filename = instance.zip_file.name.split("/")[1]

            if (instance.total_question_errors +
                    instance.total_document_errors == 0):
                theresponse = FileResponse(instance.zip_file)
                theresponse[
                    'Content-Disposition'] = 'attachment; filename="' + filename + '"'
                logger.info("[" + str(instance.transaction) + "] " +
                            ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
                instance.cleanup()
                return theresponse
            else:
                #Serializer to query only the records that contain errors

                serialized_data = QuestionLibraryErrorSummarySerializer(
                    instance)

                logger.info(
                    "[" + str(instance.transaction) + "] " +
                    ">>>>>>>>>>Transaction Finished with errors>>>>>>>>>>")

                theresponse = JsonResponse(serialized_data.data, status=201)
                instance.cleanup()
                return theresponse

        return JsonResponse(serializer.errors, status=400)


class WordToJsonZip(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthenticationWithBearer]
    serializer_class = WordToJsonZipSerializer

    @extend_schema(
        # override default docstring extraction
        description=
        'Upload a Word document(.docx) and receive a Zip package with Json included',
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

        is_random = False
        if 'randomize' in request.POST:
            if request.POST['randomize'].lower() in ("true", "yes"):
                is_random = True

        convertserializer = WordToJsonZipSerializer(data={
            'temp_file': file_obj2,
            'randomize': is_random
        })

        if convertserializer.is_valid():
            instance = convertserializer.save()

            question_library = QuestionLibrary.objects.get(
                transaction=instance.transaction.id)

            question_library_serializer = QuestionLibrarySerializer(
                question_library)
            import json
            # print(json.dumps(question_library_serializer.data, indent=4))
            jsonfile = ContentFile(str(
                json.dumps(question_library_serializer.data, indent=4)),
                                   name="output.json")
            instance.json_file = jsonfile
            instance.save()
            if instance.total_document_errors == 0:
                instance.create_zip_file_package()

                filename = instance.output_zip_file.name.split("/")[1]
                file_response = FileResponse(instance.output_zip_file)
                file_response[
                    'Content-Disposition'] = 'attachment; filename="' + filename + '"'

                logger.info("[" + str(instance.transaction) + "] " +
                            ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
                instance.cleanup()
                return file_response
            else:
                #Query only the records that contain errors
                serialized_data = QuestionLibraryErrorSummarySerializer(
                    instance)
                theresponse = JsonResponse(serialized_data.data, status=400)

                logger.info(
                    "[" + str(instance.transaction) + "] " +
                    ">>>>>>>>>>Transaction Finished with document error>>>>>>>>>>"
                )
                instance.cleanup()
                return theresponse

            # return Response("None")
        return JsonResponse(convertserializer.errors, status=400)


class WordToJson(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthenticationWithBearer]
    serializer_class = WordToJsonSerializer

    @extend_schema(
        # override default docstring extraction
        description='Upload a Word document(.docx) and receive a JSON string',
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

            question_library = QuestionLibrary.objects.get(
                transaction=instance.transaction.id)
            question_library_serializer = QuestionLibrarySerializer(
                question_library)

            instance.cleanup()
            return JsonResponse(question_library_serializer.data, status=200)

            # return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)


class RootPath(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        from .models import StatusResponse
        from .serializers import StatusResponseSerializer

        status = StatusResponse(name='qcon-api',
                                cluster_env=settings.CLUSTER_ENV,
                                version_number=settings.GIT_TAG,
                                build_env=settings.BUILD_ENV,
                                build_hash=settings.BUILD_HASH,
                                build_short_sha=settings.BUILD_SHORT_SHA,
                                build_date=settings.BUILD_DATE,
                                app_description=settings.APP_DESCRIPTION,
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