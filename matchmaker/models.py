from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from ordered_model.models import OrderedModel
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

class User(AbstractUser):
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=8, choices=GENDER_CHOICES)


	def get_age(self):
		born = self.date_of_birth
		today = date.today()
		age = today.year - born.year - (( today.month, today.day ) < (born.month, born.day))
		return age


	def get_matches(self):
		return	User.objects.exclude(gender__iexact=self.gender)


class Membership(OrderedModel, TimeStampedModel):
	title = models.CharField(max_length=50)
	messaging = models.PositiveIntegerField(default=5)
	can_see_visitors = models.BooleanField(default=True)

	def __str__(self):
		return self.title

class Category(TimeStampedModel):
	name = models.CharField(max_length=60)
	slug = models.SlugField(unique=True)
	parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Interest(TimeStampedModel):
	name = models.CharField(max_length=160)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	color = models.CharField(max_length=15, default='teal')

	class Meta:
		ordering = ['category', 'name']

	def __str__(self):
		return self.name


class UserProfile(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	about = models.CharField(null=True, blank=False, max_length=160)
	membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
	language = models.CharField(max_length=16,null=True, choices=LANGUAGE_CHOICES)
	location = models.GenericIPAddressField(null=True)
	city = models.CharField(max_length=20, null=True)
	visitors_view_count = models.PositiveIntegerField(default=0)
	contacts  = models.ManyToManyField(User, related_name='contacts_list')
	visitors = models.ManyToManyField(User, related_name='visitors_list')
	blockedUsers = models.ManyToManyField(User, related_name='blockedUsers_set')
	views = models.PositiveIntegerField(default=0, editable=False)
	interests = models.ManyToManyField(Interest, related_name='interested_users')

	def viewed(self):
		self.views = models.F('views') + 1
		self.save()

	def __str__(self):
		return "%s's Profile" % self.user.username


class Photo(TimeStampedModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userphotos')
	image = models.ImageField(upload_to='uploads/user_photos')
	viewed_by = models.ManyToManyField(User, related_name='photoviewby_list')
	public =  models.BooleanField(default=False)
	views = models.PositiveIntegerField(default=0, editable=False)

	def viewed(self):
		self.views = models.F('views') + 1
		self.save()
		
class Likes(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='likes')
	likedUsers = models.ManyToManyField(User, related_name='likedusers')
	likedPhotos = models.ManyToManyField(Photo, related_name='likedphotos')



class BasicInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basicinfo')
	ethnicity = models.CharField(max_length=20,  default='-', choices=ETHINICITY_CHOICES)
	religion = models.CharField(max_length=20,  default='-', choices=RELIGION_CHOICES)
	sign = models.CharField(max_length=20,  default='-', choices=SIGN_CHOICES)
	body_type = models.CharField(max_length=20,  default='-', choices=BODY_TYPE_CHOICES)



class StatusInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='statusinfo')
	sexual_orientation = models.CharField(max_length=20,blank=True, default='-', choices=SEXUAL_ORIENTATION_CHOICES)
	relationship_status = models.CharField(max_length=20,blank=True, default='-', choices=REL_STATUS_CHOICES)
	relationship_type = models.CharField(max_length=20,blank=True, default='-', choices=REL_TYPE_CHOICES)



class PersonalInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personalinfo')
	children =  models.CharField(max_length=20,blank=True, default='-', choices=CHILDREN_CHOICES)
	pets = models.CharField(max_length=20,blank=True, default='-', choices=PETS_CHOICES)
	car =  models.BooleanField(default=False, blank=True, choices=CAR_CHOICES)
	home_ownership = models.CharField(max_length=20,blank=True, default='-', choices=HOME_OWNERSHIP_CHOICES)
	


class ProfessionalInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professionalinfo')
	profession = models.CharField(max_length=20,blank=True, default='-', choices=PROFESSION_CHOICES)
	industry = models.CharField(max_length=20,blank=True, default='-', choices=INDUSTRY_CHOICES)
	education = models.CharField(max_length=20,blank=True, default='-', choices=EDUCATION_CHOICES)



class HabitInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='habitinfo')
	smoking =  models.CharField(max_length=20,blank=True, default='-', choices=SMOKING_CHOICES)
	drinking = models.CharField(max_length=20,blank=True, default='-', choices=DRINKING_CHOICES)
	drug = models.CharField(max_length=20,blank=True, default='-', choices=DRUG_CHOICES)
	diet = models.CharField(max_length=20,blank=True, default='-', choices=DIET_CHOICES)