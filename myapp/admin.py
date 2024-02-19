from django.contrib import admin
from .models import Project, Task
# Register your models here.
#? Añadir los modelos al admin

admin.site.register(Project)
admin.site.register(Task)