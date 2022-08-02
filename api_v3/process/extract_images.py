import os
import re
from ..models import Image

def extract_images(questionlibrary):
    x = re.findall(r"<img src=.*/>", questionlibrary.pandoc_output)
    if len(x) == 0:
        return
    for image in x:
        image_object = Image.objects.create(question_library=questionlibrary)
        image_object.save()
        image_object.image = image
        image_object.save()
    model_images = Image.objects.filter(question_library=questionlibrary)
    for modelimage in model_images:
        val = re.escape(modelimage.image)          
        x = re.sub(val, "<<<<"+ str(modelimage.id) +">>>>" , questionlibrary.pandoc_output)
        questionlibrary.pandoc_output = x
        questionlibrary.save()
    return len(model_images) 