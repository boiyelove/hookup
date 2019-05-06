import asyncio
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage, NotificationStream

class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		other_user = self.scope['url_route']['kwargs']['username']
		me = self.scope['user']
		thread_obj = await self.get_thread(me, other_user)
		self.thread_obj = thread_obj
		self.chat_room = thread_obj.get_channelname()
		await self.channel_layer.group_add(
			self.chat_room,
			self.channel_name
			)
		# print('chat_room is', self.chat_room, 'connected by ', me)
		await self.send({
			"type": "websocket.accept"
			})

		
	async def websocket_receive(self, event):
		# print("receive", event)
		front_text = event.get('text', None)
		if front_text is not None:
			loaded_dict_data = json.loads(front_text)
			msg = loaded_dict_data.get('message')
			msg = msg.strip()
			user = self.scope['user']
			# print('user is ', user)
			username = 'default'
			myResponse = {}
			if user.is_authenticated and msg:
				username = user.username
				new_msg = await self.create_chat_message(msg)
				myResponse.update({
				'username': username,
				'time': new_msg.timestamp,
				'timestamp': f'{new_msg.timestamp.timestamp()}'.replace('.',''),
				'other_user': self.scope['url_route']['kwargs']['username']
					})
			myResponse.update({
							'message': msg,
						})
			# print('chat_room is', self.chat_room, 'connected by ', user)
			await self.channel_layer.group_send(
				self.chat_room,
					{
						"type": "chat_message",
						"text": json.dumps(myResponse, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
					}
				)

	async def chat_message(self, event):
		await self.send({
			"type": "websocket.send",
			"text": event["text"]
			})

	async def websocket_disconnect(self, event):
		await self.channel_layer.group_discard(
			self.chat_room,
			self.channel_name
			)
		await self.send({
			"type": "websocket.close"
			})
		print("disconnected", event)

	
	@database_sync_to_async
	def create_chat_message(self, msg):
		return ChatMessage.objects.create(thread=self.thread_obj, user=self.scope['user'], message=msg)

	@database_sync_to_async
	def get_thread(self, user, other_username):
		return Thread.objects.get_or_new(user, other_username)[0]


class NotificationConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		self.user = self.scope['user']
		stream_obj = await self.get_notification()
		self.chat_room = stream_obj.get_channelname()
		await self.channel_layer.group_add(
			self.chat_room,
			self.channel_name
			)
		await self.send({
			"type": "websocket.accept"
			})

	async def websocket_receive(self, event):
		print("websock receive", event)
		await self.channel_layer.group_send(
				self.chat_room,
					{
						"type": "notification.message",
						"text": event,
					}
				)

	async def notification_message(self, event):
		await self.send({
			"type": "websocket.send",
			"text": event["text"]
			})


	async def websocket_disconnect(self, event):
		await self.channel_layer.group_discard(
			self.chat_room,
			self.channel_name
			)
		await self.send({
			"type": "websocket.close"
			})
		print("disconnected", event)


	@database_sync_to_async
	def get_notification(self):
		notify_obj, created = NotificationStream.objects.get_or_create(user = self.user)
		self.stream_obj = notify_obj
		return self.stream_obj