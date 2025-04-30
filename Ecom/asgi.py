"""
ASGI config for Ecom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from Channels_app.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecom.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application,
    'websocket': URLRouter(ws_urlpatterns)
})