from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import viewsets
from.models import Song,Singer
from .serializers import SongSerializer,SingerSerializer,SongHyperlinkSerializer,SingerSSSerializer

# Create your views here.
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    # serializer_class = SingerSerializer
    serializer_class = SingerSSSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    # serializer_class = SongSerializer
    serializer_class = SongHyperlinkSerializer