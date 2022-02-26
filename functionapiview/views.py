from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers
# Create your views here.

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
