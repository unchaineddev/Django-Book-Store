from operator import mod
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields.files import default_storage

from django.urls import reverse

from django.utils.text import slugify   # modify slug
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)  # character field 
    # author = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # or PROTECT
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    

    # If you want to use the url 
    def get_absolute_url(self):
        return reverse("book_num", args=[self.slug])


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)   # adding slug & overwrite save
    #     super().save(*args, **kwargs)  # make sure it is saved automatically.
    

    def __str__(self):
        return f'{self.title}--{self.author} ({self.rating})'
