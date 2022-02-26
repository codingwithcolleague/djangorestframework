from django.contrib import admin

# Register your models here.
from .models import Song,Singer

admin.site.register(Song)
admin.site.register(Singer)