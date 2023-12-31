from rest_framework import serializers
from .models import Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue-detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Event
        fields = ('id', 'venue_id', 'venue', 'name', 'venue_name', 'event_description', 'img_url', 'date', 'time', 'performers', 'theme', 'price', 'tickets_sold', 'tickets_available')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_url', 'name', 'location', 'capacity', 'bar', 'kitchen', 'bathrooms', 'outdoor_space', 'accessibility', 'events')

