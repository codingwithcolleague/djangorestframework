import email
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
from .customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class StudentViewsetModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [MyPermission]



# class StudentViewsetModel(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer


"""
    Function Based authentication
"""

@authentication_classes([SessionAuthentication])
@permission_classes([MyPermission])
@api_view(["GET","PUT","POST"])
def studentapi(request):
    if request.method == "GET":
        stu = Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        return Response({"data" : serializers.data})
    elif request.method == "POST":
        jsondata = request.data
        serializers = StudentSerializers(data=jsondata)
        if serializers.is_valid():
            serializers.save()
            return Response({"data" : serializers.data})
        return Response({"data" : serializers.errors})
    elif request.method == "PUT":
        id = request.data.get("id")
        stu = Student.objects.get(id=id)
        serializers = StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
        return Response({"msg" : "Data Updated" })    
    elif request.method == "Deleted":
        id = request.data.get("id")
        try:
            stu = Student.objects.get(id=id)
            return Response({"msg" : "Data deleted"})    
        except Student.DoesNotExist:
            return Response({"msg" : "Not Deleted"})     



class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializers = self.serializer_class(data=request.data, 
        context={"request":request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key,
            "user_id" : user.pk,
            "email" : user.email
        })