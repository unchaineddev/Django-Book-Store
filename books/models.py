from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)  # character field 
    author = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_best_selling = models.BooleanField(default=False)
    # id = models.AutoField() # added automatically (unique identifier)


    def __str__(self):
        return f'{self.title}--{self.author} ({self.rating})'
