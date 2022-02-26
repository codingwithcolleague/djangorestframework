from django.shortcuts import render
from rest_framework.generics import ListAPIView
from serializersapp.models import Student
from crudopration.serializers import StudentSerializers
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .mypagination import MyPageNumberPagination
# Create your views here.

class StudentFilterListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filterset_fields = ['name']
    pagination_class = MyPageNumberPagination
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)


class StudentSearchListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [SearchFilter]
    search_fields = ['name']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)



class StudentOrderListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [OrderingFilter]
    ordering_fields =  ['name']
    

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)