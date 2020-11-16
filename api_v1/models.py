from django.db import models

# Create your models here.

def tempfile_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def zipfile_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Quiz(models.Model):   
    id = models.AutoField(primary_key=True) 
    session = models.CharField(max_length=100)
    tempfile = models.FileField(upload_to=tempfile_path)
    JSON = models.JSONField(encoder=None, decoder=None)
    zipfile = models.FileField(upload_to=zipfile_path)
    state = models.DecimalField(unique=False, max_digits=2, decimal_places=0)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
