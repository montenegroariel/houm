from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


#class UserLocationViewSet(viewsets.ModelViewSet):
#    permission_classes = (IsAuthenticated,)
#    queryset = Location.objects.all()
#    serializer_class = LocationSerializer

#    def get_queryset(self):
#        queryset = self.queryset
#        location = queryset.filter(user=self.request.user)
#        return location