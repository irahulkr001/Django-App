from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    image = models.ImageField(upload_to="employee_image")