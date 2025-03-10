import json
from markupsafe import escape

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Group, Mensage
from django.contrib.auth.models import User
from django.utils import timezone, dateformat


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = escape(text_data_json["message"])
        user = text_data_json["user"]
        date = dateformat.format(timezone.localtime(timezone.now()),'M-d-Y H:i')
        print(f'{message} recebido')

        is_blocked = User.objects.get(username=user).groups.filter(name="Banned").exists()
        if not is_blocked:
            m = Mensage.objects.create(user=user, content=message, date=timezone.now(), group=Group.objects.get(name=self.room_name))
            m.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", 'message': {"is_blocked": is_blocked, "message": message, 'user': user, 'date': str(date)}}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
        pass
