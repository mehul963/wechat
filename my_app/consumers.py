from channels.generic.websocket import AsyncWebsocketConsumer,SyncConsumer
from asgiref.sync import async_to_sync,sync_to_async
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
import json

import asyncio

from .models import ChatText
from django.contrib.auth.models import User


class consumer(SyncConsumer):
    def websocket_connect(self):
        self.send({
            'type':'websocket.accept'
        })
class SenderConsumer(AsyncWebsocketConsumer):
    channels={}
    async def connect(self):
        # self.channel_name=f"custom.channelname.{self.scope['user']}"
        await self.channel_layer.group_add('chat',self.channel_name)
        user=self.scope['user']
        self.channels[str(user)]=self.channel_name
        if user.is_authenticated:
            await self.accept()
            # chat_messages = await database_sync_to_async(ChatText.objects.filter)(sender=self.scope['user'])
    async def receive(self, text_data=None, bytes_data=None):
        data=json.loads(text_data)
        receiver=await User.objects.aget(username=data['user'])
        await database_sync_to_async(ChatText(sender=self.scope['user'],receiver=receiver,text=data['msg']).save)()

        channel=self.channels.get(data.get('user'))
        if channel:
            await self.channel_layer.send(channel,{
                'type':'chat_message',
                'data':text_data
            })
        else:
            senddata={
                    "msg":f"{data['user']} ->User is not connected",
                    "user":str(self.scope['user'])
                }
            await self.send(
                json.dumps(senddata)
            )
    async def chat_message(self,message):
        try:
            await self.send(message['data'])
        except Exception as e:
            print(e)

    async def disconnect(self,*kwargs):
        self.channels.pop(str(self.scope['user']))
        self.close()
    
class SendChat(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            await self.accept()

    def getChat(self,receiver):
        receiver=User.objects.get(username=receiver)
        chat_msgs=ChatText.objects.filter(sender=self.scope['user'])
        return chat_msgs
        
    async def receive(self, text_data=None, bytes_data=None):
        data=json.loads(text_data)
        if receiver:=data.get('receiver'):
            chats=await database_sync_to_async(self.getChat)(receiver)
            await asyncio.sleep(3)
            print(chats)
            ChatText.objects.aget
            




# class SenderConsumer(AsyncWebsocketConsumer):
#     async def websocket_connect(self, message):
#         self.channel_name=self.scope["user"]
#         await self.accept()

#     async def websocket_receive(self, message):
#         print(message)
#         data=json.loads(message['text'])
#         msg=data['msg']
#         username=data['user']
#         print(username)
#         channel_layer=get_channel_layer()

#         x=await channel_layer.send('test2',
#                                  {
#                                      'type':'send_msg',
#                                      'text':msg
#                                  })
#         print(x)
#     async def send_msg(self,event):
#         print(event) 
#         print(type(event))
#     async def websocket_disconnect(self, message):
#         await self.send("Closing My self")
#         print(message)
#         return await super().websocket_disconnect(message)
