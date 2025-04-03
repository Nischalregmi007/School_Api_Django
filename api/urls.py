from home.views import addmissionapi, admissionshowapi, update_status, delete_student, update_student
from django.urls import path

urlpatterns = [
    path('admission_registration/', addmissionapi.as_view()),
    path('admissiondata_show/', admissionshowapi.as_view()),
    path('update_status/<int:student_id>/', update_status, name='update_status'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('update_student/', update_student, name='update_student'),
]