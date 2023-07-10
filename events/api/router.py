from rest_framework.routers import DefaultRouter
from events.api.views import EventApiViewSet


router_event = DefaultRouter()

router_event.register(prefix='event', basename='event',
                      viewset=EventApiViewSet)
