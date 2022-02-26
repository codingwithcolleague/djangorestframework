from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers
# Create your views here.

class StudentListMixing(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class StudentCreateMixing(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetriveMixing(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdateMixing(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDeleteMixing(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self,request,*args,**kwargs):
        return self.destory(request,*args,**kwargs)


class StudentListCreateMixing(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetriveUpdateMixing(GenericAPIView,UpdateModelMixin,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destory(request,*args,**kwargs)

