from django.db import models

# Create your models here.
class Feed(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=20)
    feedtype=models.CharField(max_length=20)
    msg=models.CharField(max_length=100)
class Leave(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    fr=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    status=models.IntegerField()
    msg=models.CharField(max_length=100)