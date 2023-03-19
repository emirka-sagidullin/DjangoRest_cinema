from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Film)
admin.site.register(Poster)
admin.site.register(Genre)
admin.site.register(Director)