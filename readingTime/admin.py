from django.contrib import admin
from readingTime.models import Category, Book, Profile


# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Profile)
