from django.urls import path
from websocketspy import consumers

ws_urlpatterns = [
    path('', consumers.WSConsumer.as_asgi())
]