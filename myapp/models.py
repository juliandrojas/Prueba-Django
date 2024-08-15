from django.db import models

# Create your models here.
class Project(models.Model):
    # CharField = varchar
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    # TextField = Textos mas largos
    description = models.TextField()
    # ForeignKey = relaciona con otro modelo
    # on_delete = cascade, para que si se elimina la relación se borren todos los datos asociados
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 