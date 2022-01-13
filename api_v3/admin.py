# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.contrib import admin

# Register your models here.

from .models import QuestionLibrary, Section

admin.site.register(QuestionLibrary)
admin.site.register(Section)