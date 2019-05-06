from djang.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layers
from asgiref.sync import async_to_sync
from .models import ChatMessage


@receiver(post_save, sender=ChatMessage)
def create_notification(sender, instance, created, **kwargs):
	if created:
		other_user = instance.get_otheruser()
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			other_user.notificationstream.get_channelname(),
			{
				"type": "user.new_message",
				"text": f"{instance.user.username}: {instance.message:30}"
			})
		print("In signals here")

		# check if user is connected
		# if connected, send notification



  #       "gossip", {"type": "user.gossip",
  #          "event": "New User",
  #          "username": instance.username})