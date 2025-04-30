from django.urls import path
from . import consumers

ws_urlpatterns=[
path('sc/',consumers.MySyncConsumer.as_asgi())
]