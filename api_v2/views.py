from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser

# from os import makedirs, path, walk

from .models import QuestionLibrary
from .models import Question
from .models import Transaction

from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)

from .serializers import UploadSerializer, SectionSerializer, QuestionLibrarySerializer, QuestionSerializer, TransactionSerializer
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


def print_result(task):
    print(task.result)

class GetStatus(APIView):

    serializer_class = TransactionSerializer
    def get(self, request, id):
        # question_library = QuestionLibrary.objects.get()
        # print(request.data['id'])
        transactionquery = Transaction.objects.get(id=id)

        transaction_serializer = TransactionSerializer(transactionquery)        
        return Response(transaction_serializer.data, status=200)



class GetResult(APIView):

    serializer_class = QuestionLibrarySerializer, 
    def get(self, request, id):
        # question_library = QuestionLibrary.objects.get()
        # print(request.data['id'])
        question_library = QuestionLibrary.objects.get(transaction=id)
        question_library_serializer = QuestionLibrarySerializer(question_library)
        
        return Response(question_library_serializer.data, status=200)
        # return JsonResponse(response, status=200, safe=False)


class Upload(APIView):
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
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

            return JsonResponse(response, status=201)    
        return JsonResponse(serializer.errors, status=400)

# Temporary endpoint for the admin view
class Download(APIView):
    # parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
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

    parser_classes = [MultiPartParser]
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

        QuestionModel = QuestionLibrary.objects.get(id=request.data['id'])
        serializer = SectionSerializer(QuestionModel, data={'section_name': request.data['section_name'], 'id': request.data['id']}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


