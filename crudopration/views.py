import re
from django.http import HttpResponse
from django.shortcuts import render
import io
from serializersapp.models import Student
from .serializers import StudentSerializers,StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

@csrf_exempt
def studentapi(request):
    if request.method == "GET":
        stu = Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        jsondata = JSONRenderer().render(serializers.data)
        return HttpResponse(jsondata,content_type="application/json")
    
    elif request.method == "POST":
        data = request.body
        stream = io.BytesIO(data)
        jsondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/data")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/data")

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        jsondata = JSONParser().parse(stream)
        id = jsondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res =  {"msg" : "Data updated" }
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")
        jdata = JSONParser().parse(serializer.errors)
        return HttpResponse(jdata,content_type="application/json")

    elif request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        jsondata = JSONParser().parse(stream)
        id = jsondata.get('id')
        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {"msg" : "Data Delete"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")
        except Student.DoesNotExist as e:
            res = {"msg" : "Data not found"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")




@method_decorator(csrf_exempt , name='dispatch' )
class StudentView(View):
    def get(self,request):
        stu = Student.objects.all()
        serializers = StudentModelSerializer(stu,many=True)
        # serializers = StudentSerializers(stu,many=True)
        jsondata = JSONRenderer().render(serializers.data)
        return HttpResponse(jsondata,content_type="application/json")

    def post(self,request):
        data = request.body
        stream = io.BytesIO(data)
        jsondata = JSONParser().parse(stream)
        serializer = StudentModelSerializer(data=jsondata)
        # serializer = StudentSerializers(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/data")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/data")

    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        jsondata = JSONParser().parse(stream)
        id = jsondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentModelSerializer(stu,data=jsondata,partial=True)
        # serializer = StudentSerializers(stu,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res =  {"msg" : "Data updated" }
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")
        jdata = JSONParser().parse(serializer.errors)
        return HttpResponse(jdata,content_type="application/json")

    def delete(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        jsondata = JSONParser().parse(stream)
        id = jsondata.get('id')
        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {"msg" : "Data Delete"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")
        except Student.DoesNotExist as e:
            res = {"msg" : "Data not found"}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type="application/json")