from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    # we want each category (i.e.: Fiction) to be unique
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_books(self):
        return Book.objects.filter(categories__title=self.title)

    def __str__(self):
        return self.name;

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    synopsis = models.CharField(max_length=1000)
    personal_rating = models.IntegerField()
    global_rating = models.IntegerField()
    in_read_list = models.BooleanField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    # Linking UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40,
                                  default='first name', blank=False)
    last_name = models.CharField(max_length=40,
                                 default='last name', blank=False)
    email = models.EmailField(max_length=150,
                              default='example1@example.com', blank=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created == True:
        Profile.objects.create(user=instance)
    instance.profile.save()



