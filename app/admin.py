from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .models import Volunteer
from .models import BookNow


admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(BookNow)