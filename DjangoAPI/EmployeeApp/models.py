from django.db import models


# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)


class BasicInformations(models.Model):
    BIid = models.AutoField(primary_key=True)
    BIregDate = models.DateField()
    BIaddress = models.CharField(max_length=100)
    BIworkTime = models.CharField(max_length=100)
    BItelephone = models.CharField(max_length=100)
    BIfaxes = models.CharField(max_length=100)
    BIemail = models.CharField(max_length=100)
    BIaddressPlace = models.CharField(max_length=100)
