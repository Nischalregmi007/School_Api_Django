from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import StudentSerializer
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