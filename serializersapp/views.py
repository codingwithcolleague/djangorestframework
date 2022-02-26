from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import  JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def student_details(request):
    student = Student.objects.get(id=1)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg" : "Data Created"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)        
        return HttpResponse(json_data,content_type="application/json")
