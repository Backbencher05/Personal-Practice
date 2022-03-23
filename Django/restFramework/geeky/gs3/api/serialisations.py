from rest_framework import serializers


class StudentSerialiser(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    roll = serializers.IntegerField()
    addr = serializers.CharField(max_length=60)
