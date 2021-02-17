from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .serializers import QuestionLibrarySerializer, WordToZipSerializer, WordToJsonSerializer, WordToJsonZipSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser

from django.core.files.base import ContentFile
# from os import makedirs, path, walk

from .models import QuestionLibrary
from .models import Question
from .models import Transaction

from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)
WordToJsonZip_Logger = logging.getLogger(
    'api_v2.views.WordToJsonZip')

WordToZip_Logger = logging.getLogger(
    'api_v2.views.WordToZip')


class WordToZip(APIView):
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
    serializer_class = WordToZipSerializer

    @extend_schema(
        # override default docstring extraction
        description='Upload a Word document(.docx) and receive a zip(.zip) file',
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
        serializer = WordToZipSerializer(data={'temp_file': file_obj2})

        if serializer.is_valid():
            instance = serializer.save()

            WordToZip_Logger.info("["+str(instance.transaction) + "] " +
                                      ">>>>>>>>>>Transaction Finished>>>>>>>>>>")

            filename = instance.zip_file.name.split("/")[1]
            file_response = FileResponse(instance.zip_file)
            file_response['Content-Disposition'] = 'attachment; filename="'+filename + '"'
            return file_response
            # return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)


class WordToJsonZip(APIView):
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
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
        convertserializer = WordToJsonZipSerializer(
            data={'temp_file': file_obj2})

        if convertserializer.is_valid():
            instance = convertserializer.save()

            question_library = QuestionLibrary.objects.get(
                transaction=instance.transaction.id)
            question_library_serializer = QuestionLibrarySerializer(
                question_library)

            jsonfile = ContentFile(
                str(question_library_serializer.data), name="output.json")
            instance.json_file = jsonfile
            instance.save()

            instance.create_zip_file_package()

            WordToJsonZip_Logger.info("["+str(instance.transaction) + "] " +
                                      ">>>>>>>>>>Transaction Finished>>>>>>>>>>")

            filename = instance.output_zip_file.name.split("/")[1]
            file_response = FileResponse(instance.output_zip_file)
            file_response['Content-Disposition'] = 'attachment; filename="'+filename + '"'
            return file_response

            # return Response("None")
        return JsonResponse(convertserializer.errors, status=400)


class WordToJson(APIView):
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
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

            return JsonResponse(question_library_serializer.data, status=200)

            # return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)


# Temporary endpoint for the admin view
# class Download(APIView):
#     # parser_classes = [MultiPartParser]
#     # permission_classes = [IsAuthenticated]
#     # serializer_class = UploadSerializer
#     def get(self, request , id, filename):
#         FILE = './temp/' + str(id) + '/' + filename
#         file_response = FileResponse(open(FILE, 'rb'))
#         return file_response
