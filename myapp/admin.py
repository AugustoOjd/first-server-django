from django.contrib import admin
from .models import Project, Task
# importa los modelos para usar esa base de datos en admin

# Register your models here.

admin.site.register(Project)

# importar task de la misma manera

admin.site.register(Task)
