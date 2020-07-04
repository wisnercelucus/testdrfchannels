from django.urls import path

from channels.auth import AuthMiddlewareStack

from channels.routing import ProtocolTypeRouter, URLRouter

from posts.consumers import NotificationConsumer


websockets = URLRouter([
    path(
        "ws/notifications/",
        NotificationConsumer,
        name="ws_notifications",
    ),
])


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(websockets),
})