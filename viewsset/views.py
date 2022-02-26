from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets

class StudentViewset(viewsets.ViewSet):

    def list(self,request):
        print("base" , self.basename)
        print("action" , self.action)
        print("suffix" , self.suffix)
        print("name" , self.name)
        print("description" , self.description)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):
        if pk is not None:
            stu =Student.objects.get(id=pk)
            serializers = StudentSerializers(stu)
            return Response(serializers.data)

    

    def update(self,request,pk=None):
        if pk is not None:
            jsondata = request.data
            stu =Student.objects.get(id=pk)
            serializers = StudentSerializers(stu,data=jsondata,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors)
        return Response({"msg" : "Data updated"})

    
    def partial_update(self,request,pk=None):
        if pk is not None:
            jsondata = request.data
            stu =Student.objects.get(id=pk)
            serializers = StudentSerializers(stu,data=jsondata,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors)
        return Response({"msg" : "Data updated"})


    
    def create(self,request):
        jsondata = request.data
        serializers = StudentSerializers(data=jsondata)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
        return Response({"msg" : "Data updated"})

    
    def destory(self,request,pk=None):
        stu = Student.objects.get(id=pk)
        stu.delete()