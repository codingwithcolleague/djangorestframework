from functools import partial
from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers
from rest_framework import status
# Create your views here.

class StudentApi(APIView):

    def get(self,request,pk=None):
        stu = Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        return Response(serializers.data)
    
    def post(self,request,pk=None,format=None):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg" : "Message created"}, status=status.HTTP_200_OK)
        return Response({"msg" : "Message created"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        print("iddd" , pk)
        id = request.data.get("id")
        stu = Student.objects.get(id=id)
        serializers = StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg" : "Data updated"}, status=status.HTTP_200_OK)
        return Response({"msg" : "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        # id = request.data.get("id")
        try:
            stu = Student.objects.get(id=id)
            return Response({"msg" : "Data Deleted"}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"msg" : "Error"}, status=status.HTTP_400_BAD_REQUEST)
