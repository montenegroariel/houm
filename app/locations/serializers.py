from django.contrib.auth.models import User
from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    #date_time = serializers.DateTimeField()

    class Meta:
            model = Location
            fields = ['pk', 'user','latitude', 'longitude', 'date_time']

    def save(self, **kwargs):
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)            