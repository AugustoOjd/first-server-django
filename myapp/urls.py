from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # <variable> declarar una variable dentro de la ruta, puede ser varios tipos pero se deben declarar
    # path('about/<int:id>', views.about),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    # recibiendo un id de timpo numero
    # path('tasks/<int:id>', views.tasks)
    
    # recibiendo un html
    path('tasks/', views.tasks, name='tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('create_project', views.create_project, name='create_project'),
    
]