from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class CompleteModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
class TrashModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    