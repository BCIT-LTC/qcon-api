from django.db import models

# Create your models here.

import logging
logger = logging.getLogger(__name__)

from os import makedirs, path

def format_file_path(instance, file_name):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.id, file_name)


class Quiz(models.Model):   
    id = models.AutoField(primary_key=True) 
    # session = models.CharField(max_length=100, null=True)
    folder_path = models.FilePathField(path=None, match=None, recursive=False, max_length=None)
    temp_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    pandoc_string = models.TextField(blank=True, null=True)
    xml_string = models.TextField(blank=True, null=True)
    xml_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    zip_file = models.FileField(upload_to=format_file_path, blank=True, null=True)
    # tempfile = models.FileField(upload_to='file_newww', blank=True, null=True)
    # JSON = models.JSONField(encoder=None, decoder=None, blank=True, null=True)
    # state = models.DecimalField(unique=False, max_digits=2, decimal_places=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def create_directory(self):
        # self.folder_path('/code/temp/' + str(self.id))
        if not path.exists(self.folder_path):
            makedirs(self.folder_path)
    
    def __str__(self):
        return str(self.id)

    