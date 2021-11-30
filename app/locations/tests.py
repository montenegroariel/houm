import time
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Location
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import TimeViewSet
from rest_framework.test import APIRequestFactory

class RedirectAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='12345')
        location1 = Location(user=self.user,latitude='-58.1996264',longitude='-26.1841717')
        location1.save()
        time.sleep(5)
        location2 = Location(user=self.user,latitude='-58.1996264',longitude='-26.1841717')
        location2.save()
        time.sleep(5)
        location3 = Location(user=self.user,latitude='-58.2037251',longitude='-26.185044')
        location3.save()
        time.sleep(5)
        location4 = Location(user=self.user,latitude='-58.2005052',longitude='-26.1682231')
        location4.save()
        return super().setUp()
    
    def test_create_location(self):
        user = User.objects.create_user(username='admin', password='12345')
        self.client.force_login(user=user)

        response = self.client.post(
                '/locations/', {
                'latitude': '1',
                'longitude': '1',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_perms_create_location(self):

        response = self.client.post(
                '/locations/', {
                'latitude': '-58.1996264',
                'longitude': '-26.1841717',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    

    def test_get_time(self):
        user = User.objects.create_user(username='time', password='12345')
        self.client.force_login(user=user)
        response = self.client.get('/locations/time/3')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_velocity(self):
        user = User.objects.create_user(username='velocity', password='12345')
        self.client.force_login(user=user)
        locations = Location.objects.all()
        for l in locations:
            print(l.user.id)
        response = self.client.get('/locations/velocity/5/0.01/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            