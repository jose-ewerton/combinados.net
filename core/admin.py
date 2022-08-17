from django.contrib import admin

from .models import User, Event, Task

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Task)