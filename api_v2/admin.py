# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.contrib import admin

# Register your models here.

from .models import Transaction, QuestionLibrary, Question, Answer, Fib, DocumentError, QuestionError

admin.site.register(Transaction)
admin.site.register(QuestionLibrary)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Fib)

admin.site.register(DocumentError)
admin.site.register(QuestionError)