from django.urls import re_path

from . import costumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", costumers.ChatConsumer.as_asgi()),
]