from django.db import models

# Create your models here.
class Admission_data(models.Model):
    course=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.IntegerField()
    studied_at=models.CharField(max_length=20)
    parent_name=models.CharField(max_length=20)
    parent_number=models.IntegerField()
    status = models.CharField(max_length=20, default="Not_approved")

