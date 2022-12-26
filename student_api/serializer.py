from .models import student1
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student1
        fields = '__all__'