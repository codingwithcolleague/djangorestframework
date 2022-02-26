from rest_framework import  serializers
from serializersapp.models import Student

## crtl + shift + python interpreter


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200 )
    age = serializers.IntegerField()
    country = serializers.CharField(max_length=200 )

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    
   
    def validate_name(self,name):
        if name is not "rahul":
            raise serializers.ValidationError("Name is error")
        return name

    def validate(self,data):
        name = data.get("name")
        if name is not "rahul":
            raise serializers.ValidationError("Name is error")
        return name