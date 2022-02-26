from pyexpat import model
from random import choices
from attr import field
from rest_framework import serializers

from serializersapp.models import Student

COUNTRY_CHOICES = (
    ('In','India'),
    ('asia', 'Asia'),
    ('america','America'),
    ('usa','USA'),
)

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    country = serializers.ChoiceField(choices=COUNTRY_CHOICES)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name" , instance.name)
        instance.age = validated_data.get("age",instance.age)
        instance.country = validated_data.get("country",instance.country)
        instance.save()
        return instance


    # def validate_name(self,name):
    #     if name is not "rahul":
    #         raise serializers.ValidationError("Name is error")
    #     return name

    def validate(self,data):
        name = data.get("name")
        print("nameee" , name)
        if name == "rahul":
            raise serializers.ValidationError("Name is error")
        return data
        

class StudentModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Student
        fields = ['id','name' , 'age' , 'country']
        # read_only_fields = ['name']