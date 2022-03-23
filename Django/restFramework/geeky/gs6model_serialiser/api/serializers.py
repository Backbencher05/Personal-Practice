#from django.db.models import fields
#from django.db.models.base import Model
#from django.db.models.constraints import BaseConstraint
from rest_framework import serializers
from api.models import Student

# Model serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        
# model serializers me sbb kuch mill jata h 
# hmko algg se 

# fields bhi nhi banani 
# create and update function bhi nhi define krna

# Noral serializer
'''
# Validators
def start_with_r(value):
 if value[0].lower() != 'r':
  raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.Serializer):
 name= serializers.CharField(max_length=100, validators=[start_with_r])
 roll = serializers.IntegerField()
 city= serializers.CharField(max_length=100)

 def create(self, validated_data):
  return Student.objects.create(**validated_data)

 def update(self, instance, validated_data):
  # print(instance.name)
  instance.name = validated_data.get('name', instance.name)
  # print(instance.name)
  instance.roll = validated_data.get('roll', instance.roll)
  instance.city = validated_data.get('city', instance.city)
  instance.save()
  return instance

 # Field Lavel Validation
 def validate_roll(self, value):
  if value >= 200:
   raise serializers.ValidationError('Seat Full')
  return value

 # Object Level Validation
 def validate(self, data):
  nm = data.get('name')
  ct = data.get('city')
  if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
   raise serializers.ValidationError('City must be Ranchi')
  return data
'''