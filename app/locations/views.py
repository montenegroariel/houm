from datetime import datetime
from django.db.models.fields import CharField, DateField, DurationField, TimeField
from rest_framework import permissions
from .models import Location
from .serializers import LocationSerializer, TimeSerializer, VelocitySerializer
from django.shortcuts import render
from rest_framework import serializers, viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Func, Avg
from django.db import models
from django.db.models import DateTimeField, ExpressionWrapper, F
from math import sin, cos, sqrt, atan2, radians


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            location = Location.objects.filter(user=request.user, latitude=request.data['latitude'], longitude=request.data['longitude']).last()
            if location:
                location.end = datetime.now()
                location.save()
                return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)            
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSerializer

    def list(self, request, *args, **kwargs):
        time_list=[]
        user_id = kwargs["user_id"]
        locations = Location.objects.filter(user_id=user_id)
        for location in locations:
            time_list.append({
                "user" : location.user,
                "latitude" : location.latitude,
                "longitude" : location.longitude,
                "time": str(location.end - location.begin),
            })
        time = TimeSerializer(instance=time_list, many=True)
        return Response(time.data)
    

class VelocityViewSet(generics.ListAPIView):
    permissions_classes = (IsAuthenticated,)
    serializers_class = VelocitySerializer

    def list(self, request, *args, **kwargs):
        user_id = kwargs["user_id"]
        velocity_list=[]
        locations = Location.objects.filter(user_id=user_id)
        velocity = 0
        distance = 0
        latitude_start = locations.first().latitude
        longitude_start = locations.first().longitude
        time_start = locations.first().end
        for location in locations:
            velocity_list.append({
                "user" : location.user,
                "latitude_start" : latitude_start,
                "longitude_start" : longitude_start,
                "latitude_end" : location.latitude,
                "longitude_end" : location.longitude,
                "time_start" : time_start,
                "time_end" : location.end,                
                "velocity": velocity,
                "distance" : distance,
            })
            latitude_start = velocity_list[-1]["latitude_end"]
            longitude_start = velocity_list[-1]["longitude_end"]
            time_start =  velocity_list[-1]["time_end"]
        
            distance = self.get_distance(velocity_list[-1]["latitude_start"], 
                                        velocity_list[-1]["longitude_start"],
                                        velocity_list[-1]["latitude_end"], 
                                        velocity_list[-1]["longitude_end"])

            velocity = self.get_velocity(distance, velocity_list[-1]["time_start"], velocity_list[-1]["time_end"])
        result = filter(lambda x: x["velocity"] > kwargs["velocity"], velocity_list)
        total = VelocitySerializer(instance=result, many=True)
        return Response(total.data)


    def get_distance(self, lat1,lon1,lat2,lon2):      
        R = 6371 # Radius of the earth in km
        dLat = radians(lat2-lat1)
        dLon = radians(lon2-lon1)
        rLat1 = radians(lat1)
        rLat2 = radians(lat2)
 
        a = sin(dLat/2) * sin(dLat/2) + cos(rLat1) * cos(rLat2) * sin(dLon/2) * sin(dLon/2) 
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c # Distance in km
        return round(distance,2)

    def get_velocity(self, dist_km, time_start, time_end):
        return dist_km / (time_end - time_start).seconds if time_end > time_start else 0