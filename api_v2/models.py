from os import makedirs, path
from django.db import models

import pypandoc

from api_v2.questionsplitter.L1Converter import L1Converter
from api_v2.parser.QuestionParserMain import question_parser
# import api_v2.parser.QuestionParserMain

# Create your models here.

import logging
logger = logging.getLogger(__name__)
RunConversion_Logger = logging.getLogger('api_v2.models.create_pandocstring')

def format_file_path(instance, file_name):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # print('{0}/{1}'.format(instance.id, file_name))
    return '{0}/{1}'.format(instance.transaction, file_name)

# TODO format_media_path for custom media folder


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    # will be generated from TOKEN authentication in the future
    client = models.TextField(blank=True, null=True)
    progress = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " Client: " + str(self.client)


class QuestionLibrary(models.Model):
    # id = models.AutoField(primary_key=True)
    transaction = models.OneToOneField(
        Transaction, on_delete=models.CASCADE, primary_key=True)
    folder_path = models.FilePathField(
        path="/code", match=None, recursive=False, max_length=None)
    temp_file = models.FileField(
        upload_to=format_file_path, blank=True, null=True)
    randomize_answer = models.BooleanField(blank=True, null=True, default=None)
    section_name = models.TextField(blank=True, null=True)
    image_path = models.FilePathField(
        path=None, match=None, recursive=False, max_length=None)
    pandoc_string = models.TextField(blank=True, null=True)
    imsmanifest_string = models.TextField(blank=True, null=True)
    imsmanifest_file = models.FileField(
        upload_to=format_file_path, blank=True, null=True)
    questiondb_string = models.TextField(blank=True, null=True)
    questiondb_file = models.FileField(
        upload_to=format_file_path, blank=True, null=True)
    zip_file = models.FileField(
        upload_to=format_file_path, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    error = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "question libraries"

    def create_directory(self):
        # self.folder_path('/code/temp/' + str(self.id))
        if not path.exists(self.folder_path):
            makedirs(self.folder_path)

    def create_pandocstring(self):

        RunConversion_Logger.info("["+str(self.transaction) + "] " +
                                  "<<<<<<<<<<Transaction Started<<<<<<<<<<")
        try:

            pandocstring = pypandoc.convert_file(self.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables+startnum', extra_args=[
                '--extract-media=' + self.folder_path, '--no-highlight', '--self-contained', '--atx-headers', '--preserve-tabs', '--wrap=preserve', '--indent=false'])

            self.pandoc_string = "\n" + pandocstring
            # raise Exception('')
            RunConversion_Logger.info(
                "["+str(self.transaction) + "] " + "Markdown String Created")
            self.transaction.progress = 1
            self.transaction.save()
            self.save()
        except Exception as e:
            RunConversion_Logger.error(
                "["+str(self.transaction) + "] " + "Markdown String Failed")
            self.error = "System Error: 1"
            self.save()

    def run_parser(self):
        try:
            L1_result = L1Converter(self)
            L1_result = "\n" + L1_result
            parsed_questions_result = question_parser(self, L1_result)
            # print(parsed_questions_result)
            self.save()
            # # raise Exception('')
            RunConversion_Logger.info(
                "["+str(self.transaction) + "] " + "Parser Finished")
            
            self.transaction.progress = 2
            self.transaction.save()
        except Exception as e:
            RunConversion_Logger.error(
                "["+str(self.transaction) + "] " + "Parser Failed")
            
            self.error = "System Error: 2"
            self.save()



    def __str__(self):
        return str(self.transaction)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_library = models.ForeignKey(
        QuestionLibrary, related_name='questions', on_delete=models.CASCADE)
    prefix = models.CharField(max_length=5, null=False)
    question_type = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=250, null=False)
    points = models.DecimalField(
        unique=False, max_digits=2, decimal_places=1, blank=True, null=True)
    randomize_answer = models.BooleanField(blank=True, null=True, default=None)
    question_body = models.TextField(blank=True, null=True)
    question_feedback = models.TextField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    correct_answers_length = models.PositiveBigIntegerField(
        blank=True, null=True, default=0)
    error = models.TextField(blank=True, null=True)

    def get_answers(self):
        return Answer.objects.filter(question=self.id)

    def get_fib(self):
        return Fib.objects.filter(question=self.id).order_by('order')

    def get_fib_answers(self):
        return Fib.objects.filter(question=self.id, type='answer')

    def __str__(self):
        return str(self.prefix) + " Transaction" + str(self.question_library.transaction.id)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    prefix = models.CharField(max_length=5, null=False)
    answer_body = models.TextField(blank=True, null=True)
    answer_feedback = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(blank=True, null=True)
    match_left = models.TextField(blank=True, null=True)
    match_right = models.TextField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.answer_body)


class Fib(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        Question, related_name='fib', on_delete=models.CASCADE)
    type = models.CharField(max_length=7, null=False)
    text = models.TextField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
