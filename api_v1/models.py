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


class ManifestEntity(object):
	resources = []

	def __init__(self):
		del self.resources[:]
		
	def addResource(self, manifestResourceEntity):
	    self.resources.append(manifestResourceEntity)


class ManifestResourceEntity(object):
	def __init__(self, identifier, resourceType, materialType, href, title = '', linkTarget = ''):
		self.identifier = identifier
		self.resourceType = resourceType
		self.materialType = materialType
		self.href = href
		self.title = title
		self.linkTarget = linkTarget


class QuestionLibraryEntity():
    def __init__(self, file, questionFolder, imageFolder, imageLocalFolder) :

        try:

            if file is None:
                raise ValueError('File not found')

            self.zipFileName = re.sub(r'\..*', '', file.name, flags=re.IGNORECASE)
            self.questionFolder = questionFolder if questionFolder else self.zipFileName
            self.imageFolder = imageFolder if imageFolder else ''
            self.imageLocalFolder = imageLocalFolder
            
        except Exception as e:
            logging.error(e)
            raise e
        
class QuestionLibraryResponseEntity():
    def __init__(self, status, zipUrl = '', message = '') :

        self.status = status
        self.zipUrl = settings.QCON['XML_QUESTION_URL'] + zipUrl
        self.message = message