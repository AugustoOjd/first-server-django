from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # <variable> declarar una variable dentro de la ruta, puede ser varios tipos pero se deben declarar
    # path('about/<int:id>', views.about),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    # recibiendo un id de timpo numero
    # path('tasks/<int:id>', views.tasks)
    
    # recibiendo un html
    path('tasks/', views.tasks)
]