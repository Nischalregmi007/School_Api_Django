from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Admission_data
# Create your views here.

class addmissionapi(APIView):
    def post(self, request):
        data=request.data
        student=StudentSerializer(data=data)
        if student.is_valid():
            student.save()
            return Response(student.data)
        else:
            return Response(student.errors)

class admissionshowapi(APIView):
    def get(self, request):
        students=Admission_data.objects.all()
        object=StudentSerializer(students, many=True)
        return Response(object.data)
