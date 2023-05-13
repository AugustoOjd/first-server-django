from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # <variable> declarar una variable dentro de la ruta, puede ser varios tipos pero se deben declarar
    path('about/<int:id>', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks)
]