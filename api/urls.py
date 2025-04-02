from home.views import addmissionapi
from django.urls import path

urlpatterns = [
    path('admission_registration/', addmissionapi.as_view()),
]