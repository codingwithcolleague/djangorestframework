from django.shortcuts import render
from rest_framework.response import Response
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers,StudentModelSerializer
from rest_framework import viewsets
# Create your views here.


class StudentViewsetModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer



class StudentViewsetModel(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

