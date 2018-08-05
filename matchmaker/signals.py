from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from .models import (UserProfile,
					Likes,
					BasicInfo,
					StatusInfo,
					PersonalInfo,
					ProfessionalInfo,
					HabitInfo)




@receiver(post_save, sender=User)
def create_profile_req(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
		Likes.objects.create(user=instance)
		BasicInfo.objects.create(user=instance)
		StatusInfo.objects.create(user=instance)
		PersonalInfo.objects.create(user=instance)
		ProfessionalInfo.objects.create(user=instance)
		HabitInfo.objects.create(user=instance)