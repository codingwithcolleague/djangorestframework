from rest_framework import  serializers
from serializersapp.models import Student

## crtl + shift + python interpreter


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200 )
    age = serializers.IntegerField()
    country = serializers.CharField(max_length=200 )

    def create(self,validate_data):
        return Student.objects.create(**validate_data)