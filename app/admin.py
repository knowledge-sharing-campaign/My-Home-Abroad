from __future__ import unicode_literals

from django.contrib import admin
from .models import Register
from .models import Volunteer
from .models import BookNow

admin.site.register(Register)
admin.site.register(Volunteer)
admin.site.register(BookNow)