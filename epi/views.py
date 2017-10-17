# api/views.py
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from epi.models import *
from epi.serializers import *
import json
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateEntryView(generics.ListCreateAPIView):
    """This class defines the create behavior of data rest api."""
##    User.objects.create(username="mock")
    queryset = Data.objects.all()

    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new data."""
        serializer.save()

class DetailsEntryView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of data."""
    queryset = Data.objects.all()

    serializer_class = EntrySerializer

class DataView(generics.ListCreateAPIView):
    """This class handles http GET for all the data"""
    queryset = Data.objects.filter(parent=None)

    serializer_class = DataSerializer

class CountyDataView(generics.ListCreateAPIView):
    """This class handles http GET for all the county data"""
    def get_queryset(self):
        return Data.objects.filter(county=self.kwargs['pk'], parent=None)

    serializer_class = DataSerializer

class IndexView(TemplateView):
    template_name = 'index.html'
