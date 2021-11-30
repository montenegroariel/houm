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
    """The endpoint receives latitude and 
    longitude, in case of not changing 
    position the final time is updated. 
    When changing position a new record is created.

    Args:
        (float): latitude
        (float): longitude

    Returns:
        [json]: Serialized location object
    """
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check posiiton
            location = Location.objects.filter(user=request.user, latitude=request.data['latitude'], longitude=request.data['longitude']).last()

            if location:
                # Update final time
                location.end = datetime.now()
                location.save()
                return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)            
            else:
                # Create new position
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeViewSet(generics.ListAPIView):
    """The duration of time is obtained 
    in a coordinate. The difference 
    between end point and start point

    Args:
        user: Id object user in url 
        /time/<int:user>.

    Returns:
        [json]: Serialized list of locations 
        over time in each coordinate
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSerializer

    def list(self, request, *args, **kwargs):
        time_list=[]
        user_id = kwargs["user_id"] # User id in url
        locations = Location.objects.filter(user_id=user_id)

        for location in locations:
            time_list.append({
                "user" : location.user,
                "latitude" : location.latitude,
                "longitude" : location.longitude,
                "time": str(location.end - location.begin), # time in location
            })
        time = TimeSerializer(instance=time_list, many=True)
        return Response(time.data)
    

class VelocityViewSet(generics.ListAPIView):
    """The speed and distance are obtained 
    with the coordinates and the time between 
    each point.

    Args:
        user: Id object user in url 
        velocity: Float number for filter velocity.
        /time/<int:user>/<float:velocity>.

    Returns:
        [json]: Serialized list of locations 
        over time, velocity and distance.
    """
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
        
        velocity_list = filter(lambda x: x["velocity"] > kwargs["velocity"], velocity_list)
        total = VelocitySerializer(instance=velocity_list, many=True)
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