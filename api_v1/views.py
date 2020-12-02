from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


from antlr.QconLexer import QconLexer
from antlr.QconListener import QconListener
from antlr.QconParser import QconParser
from api_v1.scorm.XmlWriter import XmlWriter

from antlr4 import *
import json
import sys
import pypandoc
from zipfile import *
from os.path import basename
from os import makedirs, path, walk
from xml.dom.minidom import parseString
from django.core.files.base import ContentFile
from django.core.files import File

from .models import QuestionLibrary
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity
import xml.etree.cElementTree as ET


from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)


def print_result(task):
    print(task.result)

class CliUpload(APIView):

    # permission_classes = (IsAuthenticated,)

    parser_classes = [MultiPartParser]

    def post(self, request):

        file_obj = request.FILES.get('file')

        print("CLIUPLOAD")
        question_library = QuestionLibrary.objects.create()
        question_library.folder_path = '/code/temp/' + str(question_library.id)
        question_library.image_path = question_library.folder_path + '/media/'

        # TODO get section name from CLI/Web
        # If no section name, use file name
        question_library.section_name = path.splitext(str(file_obj.name))[0]
        question_library.save()

        question_library.create_directory()
        question_library.temp_file=file_obj
        question_library.save()

        async_task('api_v1.tasks.runconversion', question_library, hook='api_v1.views.print_result')

        return Response(question_library.id)

class GetStatus(APIView):

    def post(self, request):

        # question_library = QuestionLibrary.objects.get()
        # print(request.data['id'])
        question_library = QuestionLibrary.objects.get(id=request.data['id'])

        return Response(str(question_library.checkpoint))

def Download(request, session, filename):

    FILE = './temp/' + str(session) + '/' + filename

    file_response = FileResponse(open(FILE, 'rb'))

    return file_response

