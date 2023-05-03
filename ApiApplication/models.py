from django.db import models

# Create your models here.

# Django provides ORM that is object relational mapping

class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)