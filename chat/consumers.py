from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        pass
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        pass
    
    async def chat_message(self, event):
        pass
