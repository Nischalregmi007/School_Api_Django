from rest_framework import serializers
from .models import Admission_data
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admission_data
        fields='__all__'
    def validate(self, data):
        special_characters="!@#$%^&*()_+"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name shouldnot contain any special characters")
        return data
    def create(self, validated_data):
        query=Admission_data.objects.create(course=validated_data['course']
                                    ,name=validated_data['name']
                                    ,email=validated_data['email']
                                    ,phone_number=validated_data['phone_number']
                                    ,studied_at=validated_data['studied_at']
                                    ,parent_name=validated_data['parent_name']
                                    ,parent_number=validated_data['parent_number'])
        query.save()   
        return query