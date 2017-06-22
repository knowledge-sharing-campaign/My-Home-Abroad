from __future__ import unicode_literals

from django.contrib import admin
'''
from .models import Register
from .models import Volunteer
from .models import BookNow
'''
from app.models import Register,Volunteer,BookNow

@admin.register(Register)
class AppAdmin(admin.ModelAdmin):
	list_display = ('username','first_name', 'created_at', 'modified_at',)

@admin.register(Volunteer)
class AppVolunteer(admin.ModelAdmin):
	list_display = ('username','first_name', 'created_at', 'modified_at',)

@admin.register(BookNow)
class WebAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'created_at', 'modified_at',)
'''
admin.site.register(Register)
admin.site.register(Volunteer)
admin.site.register(BookNow)
'''
