from django.contrib import admin

from todo_api.models import Status, ToDo

# Register your models here.
 
admin.site.register(Status)
admin.site.register(ToDo)