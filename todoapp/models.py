from django.db import models


# Create your models here.
class ToDoItem(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=250)
