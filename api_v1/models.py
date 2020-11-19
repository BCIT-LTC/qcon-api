from django.db import models

# Create your models here.

import logging
logger = logging.getLogger(__name__)

def tempfile_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # logger.error("HJKAHJDFGHJLKGHJKLSFDGHJKL")

    return '{0}_{1}'.format(instance.id, filename)

    # return 'file_{0}_{1}'.format(instance.id, filename)

def zipfile_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Quiz(models.Model):   
    id = models.AutoField(primary_key=True) 
    # session = models.CharField(max_length=100, null=True)
    tempfile = models.FileField(upload_to=tempfile_path, blank=True, null=True)
    # tempfile = models.FileField(upload_to='file_newww', blank=True, null=True)
    # JSON = models.JSONField(encoder=None, decoder=None, blank=True, null=True)
    # zipfile = models.FileField(upload_to=zipfile_path, null=True)
    # state = models.DecimalField(unique=False, max_digits=2, decimal_places=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
