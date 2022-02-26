from django.db import models

COUNTRY_CHOICES = (
    ('In','India'),
    ('asia', 'Asia'),
    ('america','America'),
    ('usa','USA'),
)
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200 , null=True,blank=True)
    age = models.IntegerField()
    country = models.CharField(max_length=200 , choices=COUNTRY_CHOICES)
    passby = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name