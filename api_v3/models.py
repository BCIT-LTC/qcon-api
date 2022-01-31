# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from os import makedirs, path
from django.db import models

import pypandoc

from api_v3.parser.QuestionParserMain import question_parser

from api_v3.scorm.XmlWriter import XmlWriter
from api_v3.scorm.manifest import ManifestEntity, ManifestResourceEntity

from xml.dom.minidom import parseString
import xml.etree.cElementTree as ET
from zipfile import *
from os import makedirs, path, walk, rmdir, remove

import re
from os.path import basename
from django.core.files.base import ContentFile

# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from enum import Enum
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.

import logging
logger = logging.getLogger(__name__)


def format_file_path(instance, file_name):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # print('{0}/{1}'.format(instance.id, file_name))
    return '{0}/{1}'.format(instance.id, file_name)


# TODO format_media_path for custom media folder

# class Transaction(models.Model):
#     id = models.AutoField(primary_key=True)
#     # will be generated from TOKEN authentication in the future
#     client = models.TextField(blank=True, null=True)
#     progress = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return str(self.id)


class QuestionLibrary(models.Model):
    id = models.AutoField(primary_key=True)
    folder_path = models.FilePathField(path="/code",
                                       match=None,
                                       recursive=False,
                                       max_length=None)
    temp_file = models.FileField(upload_to=format_file_path,
                                 blank=True,
                                 null=True)
    randomize_answer = models.BooleanField(blank=True, null=True, default=None)
    image_path = models.FilePathField(path=None,
                                      match=None,
                                      recursive=False,
                                      max_length=None)
    general_header = models.TextField(blank=True, null=True)
    endanswers = models.TextField(blank=True, null=True)
    pandoc_string = models.TextField(blank=True, null=True)
    pandoc_output_file = models.FileField(upload_to=format_file_path,
                                          blank=True,
                                          null=True)
    splitter_string = models.TextField(blank=True, null=True)
    imsmanifest_string = models.TextField(blank=True, null=True)
    imsmanifest_file = models.FileField(upload_to=format_file_path,
                                        blank=True,
                                        null=True)
    questiondb_string = models.TextField(blank=True, null=True)
    questiondb_file = models.FileField(upload_to=format_file_path,
                                       blank=True,
                                       null=True)
    zip_file = models.FileField(upload_to=format_file_path,
                                blank=True,
                                null=True)
    json_file = models.FileField(upload_to=format_file_path,
                                 blank=True,
                                 null=True)
    output_zip_file = models.FileField(upload_to=format_file_path,
                                       blank=True,
                                       null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_question_errors = models.DecimalField(max_digits=2,
                                                decimal_places=0,
                                                blank=True,
                                                null=True)
    total_document_errors = models.DecimalField(max_digits=2,
                                                decimal_places=0,
                                                blank=True,
                                                null=True)

    class Meta:
        verbose_name_plural = "question libraries"


# Prevents illegal characters for the filename

    def filter_section_name(self):
        section_name = self.section_name.strip()
        section_name = section_name.lower()
        filtered_section_name = re.sub('[\W_]+', ' ', section_name).strip()
        filtered_section_name = filtered_section_name.replace(' ', '-')

        # If the file name is illegal Windows string, replace with "Converted-Exam"
        filtered_section_name = filtered_section_name.replace(
            '^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$', 'Converted-Exam',
            re.IGNORECASE)

        # Limit the filename to 30 characters
        filtered_section_name = (
            filtered_section_name[:50]
        ) if len(filtered_section_name) > 50 else filtered_section_name

        self.filtered_section_name = filtered_section_name

    def create_directory(self):
        # self.folder_path('/code/temp/' + str(self.id))
        if not path.exists(self.folder_path):
            makedirs(self.folder_path)

    def create_pandocstring(self):
        try:
            mdblockquotePath = "./api_v3/pandoc-filters/mdblockquote.lua"
            emptyparaPath = "./api_v3/pandoc-filters/emptypara.lua"
            pandoc_word_to_html = pypandoc.convert_file(
                self.temp_file.path,
                format='docx+empty_paragraphs',
                to='html+empty_paragraphs',
                extra_args=[
                    '--no-highlight',
                    '--self-contained', '--markdown-headings=atx', '--preserve-tabs',
                    '--wrap=preserve', '--indent=false'
                ])
                
            print("test folder path " +self.folder_path)
            pandoc_html_to_md = pypandoc.convert_text(
                pandoc_word_to_html,
                'markdown_github',
                format='html+empty_paragraphs',
                extra_args=[
                    '--no-highlight',
                    '--self-contained', '--markdown-headings=atx', '--preserve-tabs',
                    '--wrap=preserve', '--indent=false'
                    '--lua-filter=' + mdblockquotePath,
                    '--lua-filter=' + emptyparaPath
                ])

            self.pandoc_output_file = ContentFile("\n" + pandoc_html_to_md,
                                                  name="pandoc_output.md")

            self.save()
        except Exception as e:
            logger.error("[" + str(self.id) + "] " + "Markdown String Failed")
            self.error = "Markdown String Failed"
            self.save()

    # ImsManifest string create ===================================================================================

    def create_xml_files(self):

        try:
            parsed_questions_result = Question.objects.filter(
                question_library=self)

            parsed_xml = XmlWriter(self, parsed_questions_result)
            manifest_entity = ManifestEntity()
            manifest_resource_entity = ManifestResourceEntity(
                'res_question_library', 'webcontent', 'd2lquestionlibrary',
                'questiondb.xml', 'Question Library')
            manifest_entity.add_resource(manifest_resource_entity)
            manifest = parsed_xml.create_manifest(manifest_entity,
                                                  self.folder_path)
            parsed_imsmanifest = ET.tostring(manifest.getroot(),
                                             encoding='utf-8',
                                             xml_declaration=True).decode()
            parsed_imsmanifest = parseString(parsed_imsmanifest)
            parsed_imsmanifest = parsed_imsmanifest.toprettyxml(indent="\t")
            self.imsmanifest_string = parsed_imsmanifest
            self.save()

            logger.info("[" + str(self.transaction) + "] " +
                        "imsmanifest String Created")

            self.transaction.progress = 3
            self.transaction.save()

        except Exception as e:
            logger.error("[" + str(self.transaction) + "] " +
                         "imsmanifest String Failed")

            self.error = "imsmanifest String Failed"
            self.save()

        try:
            questiondb_string = parsed_xml.questiondb_string
            img_elements = re.findall(r"\<img.*?\>", questiondb_string,
                                      re.MULTILINE)

            for idx, img in enumerate(img_elements):
                element = re.findall(r"src=\"(.*?)\"", img, re.MULTILINE)
                new_img = '<img src="{0}" alt="{1}" />'.format(
                    'assessment-assets/' + self.filtered_section_name + '/' +
                    basename(element[0]), basename(element[0]))
                questiondb_string = questiondb_string.replace(
                    img_elements[idx], new_img)

            self.questiondb_string = questiondb_string
            self.save()

            imsmanifest_file = ContentFile(self.imsmanifest_string,
                                           name="imsmanifest.xml")
            self.imsmanifest_file = imsmanifest_file
            self.save()
            logger.info("[" + str(self.transaction) + "] " +
                        "QuestionDB String Created")

            self.transaction.progress = 4
            self.transaction.save()
        except Exception as e:
            logger.error("[" + str(self.transaction) + "] " +
                         "QuestionDB String Failed")

            self.error = "QuestionDB String Failed"
            self.save()

        try:
            questiondb_file = ContentFile(self.questiondb_string,
                                          name="questiondb.xml")
            self.questiondb_file = questiondb_file
            # question_library.checkpoint = 5;
            self.save()
            logger.info("[" + str(self.transaction) + "] " +
                        "XML files Created")
            # print(datetime.now().strftime("%H:%M:%S"), "imsmanifest.xml and questiondb.xml created!")
            self.transaction.progress = 5
            self.transaction.save()
        except Exception as e:
            logger.error("[" + str(self.transaction) + "] " +
                         "XML files Failed")
            self.error = "XML files Failed"
            self.save()

    def zip_files(self):

        try:
            with ZipFile(
                    self.folder_path + "/" + self.filtered_section_name +
                    '.zip', 'w') as myzip:
                myzip.write(self.questiondb_file.path, "questiondb.xml")
                myzip.write(self.imsmanifest_file.path, "imsmanifest.xml")
                for root, dirs, files in walk(self.image_path):
                    for filename in files:
                        myzip.write(
                            path.join(root, filename), '/assessment-assets/' +
                            self.filtered_section_name + '/' + filename)

            self.zip_file.name = str(
                self.transaction) + "/" + self.filtered_section_name + '.zip'
            self.save()
            logger.info("[" + str(self.transaction) + "] " +
                        "ZIP file Created")

            self.transaction.progress = 6
            self.transaction.save()
        except Exception as e:
            logger.error("[" + str(self.transaction) + "] " +
                         "ZIP file Failed")

            self.error = "ZIP file Failed"
            self.save()

    def create_zip_file_package(self):
        try:
            with ZipFile(self.folder_path + "/" + 'package.zip', 'w') as myzip:
                myzip.write(self.zip_file.path,
                            self.filtered_section_name + '.zip')
                myzip.write(self.json_file.path, 'result.json')

            self.output_zip_file.name = str(
                self.transaction) + "/" + 'package.zip'
            self.save()
            logger.info("[" + str(self.transaction) + "] " +
                        "ZIP file with JSON package Created")
        except Exception as e:
            logger.error("[" + str(self.transaction) + "] " +
                         "ZIP file with JSON package Failed")
            self.error = "ZIP file Failed"
            self.save()

    def cleanup(self):
        if not settings.DEBUG:
            self.delete()

    def __str__(self):
        return str(self.id)


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    question_library = models.ForeignKey(QuestionLibrary,
                                         related_name='sections',
                                         on_delete=models.CASCADE)
    validated = models.BooleanField(blank=True, null=True, default=False)
    finished_processing = models.BooleanField(blank=True,
                                              null=True,
                                              default=False)
    raw_data = models.TextField(blank=True, null=True)
    section_name = models.TextField(blank=True, null=True)
    questions_processed = models.DecimalField(max_digits=3, decimal_places=0)
    questions_expected = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return str(self.prefix) + " Transaction" + str(
            self.question_library.transaction.id)


# class Question(models.Model):
#     id = models.AutoField(primary_key=True)
#     question_library = models.ForeignKey(QuestionLibrary,
#                                          related_name='questions',
#                                          on_delete=models.CASCADE)
#     prefix = models.CharField(max_length=5, null=False)
#     question_type = models.CharField(max_length=100, null=True)
#     title = models.CharField(max_length=250, null=True)
#     points = models.DecimalField(unique=False,
#                                  max_digits=2,
#                                  decimal_places=1,
#                                  null=True)
#     randomize_answer = models.BooleanField(blank=True, null=True, default=None)
#     question_body = models.TextField(blank=True, null=True)
#     question_feedback = models.TextField(blank=True, null=True)
#     hint = models.TextField(blank=True, null=True)
#     correct_answers_length = models.PositiveBigIntegerField(blank=True,
#                                                             null=True,
#                                                             default=0)

#     # error = models.TextField(blank=True, null=True)

#     def get_answers(self):
#         return Answer.objects.filter(question=self.id)

#     def get_fib(self):
#         return Fib.objects.filter(question=self.id).order_by('order')

#     def get_fib_answers(self):
#         return Fib.objects.filter(question=self.id, type='answer')

#     def __str__(self):
#         return str(self.prefix) + " Transaction" + str(
#             self.question_library.transaction.id)

# class Answer(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.ForeignKey(Question,
#                                  related_name='answers',
#                                  on_delete=models.CASCADE)
#     prefix = models.CharField(max_length=5, null=False)
#     answer_body = models.TextField(blank=True, null=True)
#     answer_feedback = models.TextField(blank=True, null=True)
#     is_correct = models.BooleanField(blank=True, null=True)
#     match_left = models.TextField(blank=True, null=True)
#     match_right = models.TextField(blank=True, null=True)
#     order = models.PositiveSmallIntegerField(blank=True, null=True)

#     def __str__(self):
#         return str(self.answer_body)

# class Fib(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.ForeignKey(Question,
#                                  related_name='fib',
#                                  on_delete=models.CASCADE)
#     type = models.CharField(max_length=7, null=False)
#     text = models.TextField(blank=True, null=True)
#     order = models.PositiveSmallIntegerField(blank=True, null=True)

# class ErrorType(models.Model):
#     errortype = models.CharField(max_length=7, primary_key=True)
#     link = models.TextField(max_length=12, null=False)

#     def __str__(self):
#         return str(self.errortype)

# class QuestionErrorType(str, Enum):  # A subclass of Enum
#     MC1 = "MC1"
#     TF1 = "TF1"
#     TF2 = "TF2"
#     TF3 = "TF3"
#     TF4 = "TF4"
#     MS1 = "MS1"
#     MT1 = "MT1"
#     MT2 = "MT2"
#     MT3 = "MT3"
#     ORD1 = "ORD1"
#     ORD2 = "ORD2"
#     ORD3 = "ORD3"
#     FIB1 = "FIB1"
#     FIB2 = "FIB2"
#     WR1 = "WR1"
#     WR2 = "WR2"
#     HEADER1 = "HEADER1"
#     HEADER2 = "HEADER2"
#     HEADER3 = "HEADER3"
#     END1 = "END1"

# class QuestionError(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.ForeignKey(Question,
#                                  related_name='questionerrors',
#                                  on_delete=models.CASCADE)
#     # errortype = models.ForeignKey(ErrorType, related_name='errortypes', on_delete=models.CASCADE)
#     errortype = models.TextField(max_length=50,
#                                  choices=[(tag, tag.value)
#                                           for tag in QuestionErrorType
#                                           ])  # Choices is a list of Tuple)
#     message = models.TextField(max_length=50)
#     action = models.TextField(max_length=50)

#     def __str__(self):
#         return str(self.id)

# class DocumentErrorType(str, Enum):  # A subclass of Enum
#     SPLITTER1 = "SPLITTER1"
#     SPLITTER2 = "SPLITTER2"

# class DocumentError(models.Model):
#     id = models.AutoField(primary_key=True)
#     document = models.ForeignKey(QuestionLibrary,
#                                  related_name='documenterrors',
#                                  on_delete=models.CASCADE)
#     # errortype = models.ForeignKey(ErrorType, related_name='errortypes', on_delete=models.CASCADE)
#     errortype = models.TextField(max_length=50,
#                                  choices=[(tag, tag.value)
#                                           for tag in DocumentErrorType
#                                           ])  # Choices is a list of Tuple)
#     message = models.TextField(max_length=50)
#     action = models.TextField(max_length=50)

#     def __str__(self):
#         return str(self.id)


@receiver(post_delete, sender=QuestionLibrary, dispatch_uid="delete_files")
def delete_files(sender, instance, **kwargs):
    if path.exists(settings.MEDIA_ROOT + str(instance)):
        try:
            for root, dirs, files in walk(settings.MEDIA_ROOT + str(instance),
                                          topdown=False):
                for name in files:
                    remove(path.join(root, name))
                for name in dirs:
                    rmdir(path.join(root, name))
        except OSError as e:
            logger.error("[" + str(instance) + "] " + "Error deleting files")

        try:
            rmdir(settings.MEDIA_ROOT + str(instance))
        except OSError as e:
            print("Error: %s : %s" % (settings.MEDIA_ROOT, e.strerror))

    logger.info("[" + str(instance) + "] " +
                "Questionlibrary and Files Deleted")


class CustomToken1(Token):
    """
    The extended authorization token model to support tokens generated from external sources
    """
    def save(self, *args, **kwargs):
        # print(self.user)
        # print(self.key)
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()
        # return '1111111111111111111111111111111111111111'


class StatusResponse:
    def __init__(self,
                 name,
                 cluster_name,
                 version_number,
                 build_env,
                 build_hash,
                 build_short_sha,
                 build_date,
                 app_description,
                 app_tagline,
                 created=None):
        self.name = name
        self.app_description = app_description
        self.version_number = version_number
        self.build_hash = build_hash
        self.build_short_sha = build_short_sha
        self.build_date = build_date
        self.cluster_name = cluster_name
        self.build_env = build_env
        self.app_tagline = app_tagline
