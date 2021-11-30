from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    begin = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name