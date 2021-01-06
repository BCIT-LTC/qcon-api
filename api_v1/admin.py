from django.contrib import admin

# Register your models here.

from .models import QuestionLibrary, Question, Answer

admin.site.register(QuestionLibrary)
admin.site.register(Question)
admin.site.register(Answer)