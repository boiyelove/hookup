from djang.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layers
from .models import ChatMessage


@receiver(pre_save, sender=ChatMessage)
def create_notification(sender, instance, created, **kwargs):
	if created:
		channel_layer = get_channel_layer()
		channel_layer.group.send(
			instance.get_channelname,
			{
				"type": "chat.system.system-message",
				"text": notification_text
			})
		check if user is connected
		if connected, send notification