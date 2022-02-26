from django.shortcuts import render
from itsdangerous import Serializer
from serializersapp.models import Student
from rest_framework.generics import (ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,
ListCreateAPIView,RetrieveUpdateAPIView)
from crudopration.serializers import StudentSerializers
# Create your views here.

class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentCreateApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentUpdateApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentRetriveApi(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentDestoryApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
