from django.contrib.auth.models import User
from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    begin = serializers.DateTimeField(required=False)
    end = serializers.DateTimeField(required=False)

    class Meta:
            model = Location
            fields = ['pk', 'user','latitude', 'longitude', 'begin','end']

    def save(self, **kwargs):
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)

    

class TimeSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    time = serializers.DateTimeField()


class VelocitySerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    latitude_start = serializers.FloatField()
    longitude_start = serializers.FloatField()
    latitude_end = serializers.FloatField()
    longitude_end = serializers.FloatField()
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()    
    velocity = serializers.FloatField()
    distance = serializers.FloatField()
    