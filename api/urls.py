from home.views import addmissionapi, admissionshowapi
from django.urls import path

urlpatterns = [
    path('admission_registration/', addmissionapi.as_view()),
    path('admissiondata_show/', admissionshowapi.as_view()),
]