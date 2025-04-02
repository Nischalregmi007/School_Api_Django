from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Admission_data
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
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
 
@api_view(['PUT'])
def update_status(request, student_id):
    student = get_object_or_404(Admission_data, id=student_id)
    student.status = "Approved"  # ✅ Updating status
    student.save()
    return Response({"message": "Student approved successfully", "status": student.status})

@api_view(['DELETE'])
def delete_student(request, student_id):
    student = get_object_or_404(Admission_data, id=student_id)
    student.delete()
    return Response({"message": "Student deleted successfully"})
