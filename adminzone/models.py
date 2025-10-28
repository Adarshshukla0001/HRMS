from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    salary=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    qua=models.CharField(max_length=50)
    exp=models.CharField(max_length=10)

class Nfc(models.Model):
    nfcid=models.IntegerField(primary_key=True)  
    nfc=models.CharField(max_length=200)

class Salary(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    salary=models.CharField(max_length=30)
    date=models.CharField(max_length=20)
    status=models.IntegerField()

class Attend(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    date=models.CharField(max_length=20)
    status=models.IntegerField()