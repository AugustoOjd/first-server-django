from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    # charfield para titlos o texto corto
    title = models.CharField(max_length=200)
    # text field campo de texto aplio
    description = models.TextField()
    # on_delete indica que hacer si se borra una tabla padre, en modelo cascada
    # cuando es foreignkey crear _id por default, entonces solo seria project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)