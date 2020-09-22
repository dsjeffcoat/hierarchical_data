from django.contrib import admin
from .models import Genre
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Genre, DraggableMPTTAdmin)