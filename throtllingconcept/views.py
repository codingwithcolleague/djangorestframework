import email
import imp
from lib2to3.pgen2 import token
from tokenize import Token
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.response import Response
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers,StudentModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import (IsAdminUser,
IsAuthenticated,AllowAny , IsAuthenticatedOrReadOnly,  DjangoModelPermissions )
# Create your views here.
from authenticated.custompermission import  MyPermission
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from throtllingconcept.throttling import RamRateThrottle
from rest_framework.generics import ListAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentThrotallingViewsetModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,RamRateThrottle]
   

class StuList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'rahulraj'  # direct write into setting