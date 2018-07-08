from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Membership(models.Model):
	name = models.CharField(max_length=60)

class UserProfile(models.Model):
	user = models.OneToOneField(user=User, on_delete=models.CASCADE, related_name='profile')
	membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
	contacts  = models.ManyToManyField(User)
	visitors = models.ManyToManyField(User)
	blockedUsers = models.ManyToManyField(User)
	interests = models.ManyToManyField('Interest')


class Likes(models.Model):
	likedUsers = models.ManyToManyField(User)
	likedPhotos = models.ManyToManyField(Photo)

class Photo(models.Model):
	image = models.ImageField(upload_to='uploads')

class Category(models.Model):
	name = models.CharField(max_length=60)

class Interest(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category)

class BasicInfo(models.Model):
	age
	gender
	location

class
	films_and_tv_series FILMS_AND_TV_SERIES_CHOCIES
	listening_to_music	LISTENING_TO_MUSIC_CHOICES
