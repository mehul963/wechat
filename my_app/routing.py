from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/connect',consumers.SenderConsumer.as_asgi()),
    path('ws/sendchat',consumers.SendChat.as_asgi()),
]