from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from events.models import Event
from events.api.serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EventApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['event_company']
    ordering = ['event_date']
