from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .models import Volunteer

admin.site.register(User)
admin.site.register(Volunteer)