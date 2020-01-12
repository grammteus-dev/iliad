
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# from authentication.routing import websocket_urlpatterns as authentication_urlpatterns

application = ProtocolTypeRouter({
  # 'websocket': AuthMiddlewareStack(
  #   URLRouter(authentication_urlpatterns),
  # ),
})
