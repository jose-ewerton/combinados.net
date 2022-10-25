from django.contrib import admin

from .models import Profile, Combined, Task

# Register your models here.

admin.site.register(Combined)
admin.site.register(Task)
admin.site.register(Profile)