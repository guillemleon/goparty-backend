from rest_framework.serializers import ModelSerializer
from events.models import Event
from users.api.serializer import UserCompanySerializer


class EventSerializer(ModelSerializer):
    event_company_data = UserCompanySerializer(
        source='event_company', read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'event_image',
            'event_country',
            'event_city',
            'event_company_name',
            'event_date',
            'event_hour',
            'event_description',
            'event_company',
            'event_company_data',
        ]
