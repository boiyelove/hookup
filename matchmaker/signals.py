from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from .models import (User, UserProfile,
					Likes, Category,
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

@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug = slugify(instance.name)
		if instance.parent:
			parent_slug = instance.parent.slug
			slug = parent_slug + '-' + slug
		slug_exist  = Category.objects.filter(slug=slug).exists()
		if slug_exist:
			count = 0
			while slug_exist:
				slug += str(count)
				count += 1
				slug_exist  = Category.objects.filter(slug=slug).exists()
		instance.slug = slug