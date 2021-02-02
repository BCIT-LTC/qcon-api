from django.contrib import admin

# Register your models here.

from .models import QuestionLibrary, Question, Answer, Fib

admin.site.register(QuestionLibrary)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Fib)