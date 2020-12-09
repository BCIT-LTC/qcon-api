from django.db import models
# Create your models here.

import logging
logger = logging.getLogger(__name__)

from os import makedirs, path

def format_file_path(instance, file_name):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # print('{0}/{1}'.format(instance.id, file_name))
    return '{0}/{1}'.format(instance.id, file_name)

# TODO format_media_path for custom media folder

class QuestionLibrary(models.Model):   
    id = models.AutoField(primary_key=True)
    # session = models.CharField(max_length=100, null=True)
    folder_path = models.FilePathField(path="/code", match=None, recursive=False, max_length=None)
    temp_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    section_name = models.TextField(blank=True, null=True)
    image_path = models.FilePathField(path=None, match=None, recursive=False, max_length=None)
    pandoc_string = models.TextField(blank=True, null=True)
    imsmanifest_string = models.TextField(blank=True, null=True)
    imsmanifest_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    questiondb_string = models.TextField(blank=True, null=True)
    questiondb_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    zip_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    # tempfile = models.FileField(upload_to='file_newww', blank=True, null=True)
    # JSON = models.JSONField(encoder=None, decoder=None, blank=True, null=True)
    # state = models.DecimalField(unique=False, max_digits=2, decimal_places=0, blank=True, null=True)
    checkpoint = models.IntegerField(blank=True, null=True)
    checkpoint_failed  = models.IntegerField(blank=True, null=True)
    time_delta = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def create_directory(self):
        # self.folder_path('/code/temp/' + str(self.id))
        if not path.exists(self.folder_path):
            makedirs(self.folder_path)
    
    def __str__(self):
        return str(self.id)

class Question(models.Model):
    id = models.AutoField(primary_key=True) 
    question_library = models.ForeignKey(QuestionLibrary, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=250, null=False)
    question_body = models.TextField(blank=True, null=True)
    question_feedback = models.TextField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    randomize_answers = models.BooleanField(blank=True, null=True)
    points = models.DecimalField(unique=False, max_digits=2, decimal_places=1, blank=True, null=True)
    correct_answers_length = models.PositiveBigIntegerField(blank=True, null=True, default=0)
    
    def get_answers(self):
        return Answer.objects.filter(question=self.id)

    def get_fib(self):
        return Fib.objects.filter(question=self.id)

    def get_fib_answers(self):
        return Fib.objects.filter(question=self.id, type='answer')
    
    def __str__(self):
        return str(self.question_body)
    # messages = {}
    # images = []


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=5, null=False)
    answer_body = models.TextField(blank=True, null=True)
    answer_feedback = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(blank=True, null=True)
    match_left = models.TextField(blank=True, null=True)
    match_right = models.TextField(blank=True, null=True)
    order = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.answer_body)



class Fib(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, null=False)
    text = models.TextField(blank=True, null=True)