from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from .utils import (GENDER_CHOICES,
						LANGUAGE_CHOICES,
						ETHINICITY_CHOICES,
						RELIGION_CHOICES,
						SIGN_CHOICES,
						BODY_TYPE_CHOICES,
						SEXUAL_ORIENTATION_CHOICES,
						REL_STATUS_CHOICES,
						REL_TYPE_CHOICES,
						CHILDREN_CHOICES,
						PETS_CHOICES,
						CAR_CHOICES,
						HOME_OWNERSHIP_CHOICES,
						PROFESSION_CHOICES,
						INDUSTRY_CHOICES,
						EDUCATION_CHOICES,
						SMOKING_CHOICES,
						DRINKING_CHOICES,
						DRUG_CHOICES,
						DIET_CHOICES,)
# Create your models here.

class Membership(TimeStampedModel):
	messaging = models.PositiveIntegerField(default=5)
	can_see_visitors = models.BooleanField(default=True)

class Category(TimeStampedModel):
	name = models.CharField(max_length=60)
	slug = models.SlugField(unique=True)
	parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ['parent', 'name']

class Interest(TimeStampedModel):
	name = models.CharField(max_length=160)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

	class Meta:
		ordering = ['category', 'name']

class UserProfile(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
	date_of_birth = models.DateField(null=True)
	gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
	language = models.CharField(max_length=16, choices=LANGUAGE_CHOICES)
	location = models.GenericIPAddressField(null=True)
	city = models.CharField(max_length=20)
	contacts  = models.ManyToManyField(User, related_name='contacts_set')
	visitors = models.ManyToManyField(User, related_name='visitors_set')
	blockedUsers = models.ManyToManyField(User, related_name='blockedUsers_set')
	interests = models.ManyToManyField('Interest')


class Photo(TimeStampedModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userphotos')
	image = models.ImageField(upload_to='uploads/user_photos')


class Likes(TimeStampedModel):
	likedUsers = models.ManyToManyField(User, related_name='likedusers')
	likedPhotos = models.ManyToManyField(Photo, related_name='likedphotos')



class BasicInfo(TimeStampedModel):
	ethnicity = models.CharField(max_length=20, choices=ETHINICITY_CHOICES)
	religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
	sign = models.CharField(max_length=20, choices=SIGN_CHOICES)
	body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)



class StatusInfo(TimeStampedModel):
	sexual_orientation = models.CharField(max_length=20, choices=SEXUAL_ORIENTATION_CHOICES)
	relationship_status = models.CharField(max_length=20, choices=REL_STATUS_CHOICES)
	relationship_type = models.CharField(max_length=20, choices=REL_TYPE_CHOICES)



class PersonalInfo(TimeStampedModel):
	children =  models.CharField(max_length=20, choices=CHILDREN_CHOICES)
	pets = models.CharField(max_length=20, choices=PETS_CHOICES)
	car =  models.BooleanField(default=False)
	home_ownership = models.CharField(max_length=20, choices=HOME_OWNERSHIP_CHOICES)
	


class ProfessionalInfo(TimeStampedModel):
	profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES)
	industry = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
	education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)



class HabitInfo(TimeStampedModel):
	smoking =  models.CharField(max_length=20, choices=SMOKING_CHOICES)
	drinking = models.CharField(max_length=20, choices=DRINKING_CHOICES)
	drug = models.CharField(max_length=20, choices=DRUG_CHOICES)
	diet = models.CharField(max_length=20, choices=DIET_CHOICES)