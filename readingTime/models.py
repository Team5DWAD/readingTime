from django.db import models

# Create your models here.

class Category(models.Model):
    # we want each category (i.e.: Fiction) to be unique
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name;

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

