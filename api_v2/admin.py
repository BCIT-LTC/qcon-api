from django.contrib import admin

# Register your models here.

from .models import Transaction, QuestionLibrary, Question, Answer, Fib

admin.site.register(Transaction)
admin.site.register(QuestionLibrary)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Fib)