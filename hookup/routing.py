from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat.consumers import ChatConsumer, NotificationConsumer
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
    	AuthMiddlewareStack(
    		URLRouter(
    			[url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
    			url(r"^notifications/$", NotificationConsumer),]
    			)
    		)
    	)
})