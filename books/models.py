from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)  # character field 
    author = models.CharField(max_length=50)
    rating = models.IntegerField()
    # id = models.AutoField() # added automatically (unique identifier)
