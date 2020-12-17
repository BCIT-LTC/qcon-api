from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser

# from os import makedirs, path, walk

from .models import QuestionLibrary

from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)

from .serializers import UploadSerializer, SectionSerializer, StatusSerializer
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


def print_result(task):
    print(task.result)


class CliUpload(APIView):

    # permission_classes = (IsAuthenticated,)

    parser_classes = [MultiPartParser]
    serializer_class = UploadSerializer

    def post(self, request):

        file_obj = request.FILES.get('file')

        print("CLIUPLOAD")
        question_library = QuestionLibrary.objects.create()
        question_library.folder_path = '/code/temp/' + str(question_library.id)
        question_library.image_path = question_library.folder_path + '/media/'

        # TODO get section name from CLI/Web
        # If no section name, use file name

        question_library.section_name = file_obj.name.split(".")[0]
        question_library.create_directory()
        question_library.temp_file=file_obj
        question_library.save()

        async_task('api_v1.tasks.runconversion', question_library, hook='api_v1.views.print_result')

        return Response(question_library.id)

class GetStatus(APIView):

    def get(self, request, id):
        # question_library = QuestionLibrary.objects.get()
        # print(request.data['id'])
        question_library = QuestionLibrary.objects.get(id=id)

        response = {
            'status': question_library.checkpoint
        }
        
        return JsonResponse(response, status=200)

class Upload(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = UploadSerializer
    @extend_schema(
        # override default docstring extraction
        description='Upload a Word document(.docx)',
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
        serializer = UploadSerializer(data={'temp_file': file_obj2})

        if serializer.is_valid():
            instance = serializer.save()
            response = {
                'id': instance.id
            }
            # instance.folder_path = '/code/temp/' + str(instance.id)
            # instance.image_path = instance.folder_path + '/media/'
            # instance.create_directory()
            # instance.save()
            # async_task('api_v1.tasks.runconversion', instance)

            return JsonResponse(response, status=201)    
        return JsonResponse(serializer.errors, status=400)

# Temporary endpoint for the admin view
class Download(APIView):
    # parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    # serializer_class = UploadSerializer
    def get(self, request , id, filename):
        FILE = './temp/' + str(id) + '/' + filename
        file_response = FileResponse(open(FILE, 'rb'))
        return file_response

class DownloadAPI(APIView):
    @extend_schema(
        # override default docstring extraction
        description='Download the Scorm zip file package',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def get(self, request, id, format=None):
        question_library = QuestionLibrary.objects.get(id=id)
        filename=question_library.zip_file.name.split("/")[1]
        file_response = FileResponse(question_library.zip_file)
        file_response['Content-Disposition'] = 'attachment; filename="'+filename +'"' 
        return file_response
class SetSection(APIView):

    serializer_class = SectionSerializer

    @extend_schema(
        # override default docstring extraction
        description='Set the Section Name',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def post(self, request, format=None):

        serializer = SectionSerializer(data={'section_name': request.data['section_name']})

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

