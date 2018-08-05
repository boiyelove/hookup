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
	gender = models.CharField(max_length=8,null=True, choices=GENDER_CHOICES)
	language = models.CharField(max_length=16,null=True, choices=LANGUAGE_CHOICES)
	location = models.GenericIPAddressField(null=True)
	city = models.CharField(max_length=20)
	views = models.PositiveIntegerField(default=0)
	contacts  = models.ManyToManyField(User, related_name='contacts_set')
	visitors = models.ManyToManyField(User, related_name='visitors_set')
	blockedUsers = models.ManyToManyField(User, related_name='blockedUsers_set')
	interests = models.ManyToManyField('Interest')


class Photo(TimeStampedModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userphotos')
	image = models.ImageField(upload_to='uploads/user_photos')
	viewed_by = models.ManyToManyField(User, related_name='photoviewby_list')


class Likes(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	likedUsers = models.ManyToManyField(User, related_name='likedusers')
	likedPhotos = models.ManyToManyField(Photo, related_name='likedphotos')



class BasicInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ethnicity = models.CharField(max_length=20,null=True, choices=ETHINICITY_CHOICES)
	religion = models.CharField(max_length=20,null=True, choices=RELIGION_CHOICES)
	sign = models.CharField(max_length=20,null=True, choices=SIGN_CHOICES)
	body_type = models.CharField(max_length=20,null=True, choices=BODY_TYPE_CHOICES)



class StatusInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sexual_orientation = models.CharField(max_length=20,null=True, choices=SEXUAL_ORIENTATION_CHOICES)
	relationship_status = models.CharField(max_length=20,null=True, choices=REL_STATUS_CHOICES)
	relationship_type = models.CharField(max_length=20,null=True, choices=REL_TYPE_CHOICES)



class PersonalInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	children =  models.CharField(max_length=20,null=True, choices=CHILDREN_CHOICES)
	pets = models.CharField(max_length=20,null=True, choices=PETS_CHOICES)
	car =  models.BooleanField(default=False)
	home_ownership = models.CharField(max_length=20,null=True, choices=HOME_OWNERSHIP_CHOICES)
	


class ProfessionalInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profession = models.CharField(max_length=20,null=True, choices=PROFESSION_CHOICES)
	industry = models.CharField(max_length=20,null=True, choices=INDUSTRY_CHOICES)
	education = models.CharField(max_length=20,null=True, choices=EDUCATION_CHOICES)



class HabitInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	smoking =  models.CharField(max_length=20,null=True, choices=SMOKING_CHOICES)
	drinking = models.CharField(max_length=20,null=True, choices=DRINKING_CHOICES)
	drug = models.CharField(max_length=20,null=True, choices=DRUG_CHOICES)
	diet = models.CharField(max_length=20,null=True, choices=DIET_CHOICES)