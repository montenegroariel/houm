from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user