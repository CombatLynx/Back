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
    BIaddress = models.CharField(max_length=1000)
    BIworkTime = models.CharField(max_length=1000)
    BItelephone = models.CharField(max_length=1000)
    BIfaxes = models.CharField(max_length=1000)
    BIemail = models.CharField(max_length=1000)
    BIaddressPlace = models.CharField(max_length=1000)


# УЧРЕДИТЕЛИ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ
class UchredsInformation(models.Model):
    UBIid = models.AutoField(primary_key=True)
    UBIrow = models.CharField(max_length=100000)


# СТРУКТУРНЫЕ ПОДРАЗДЕЛЕНИЯ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ
class DepartmentsInformation(models.Model):
    DIid = models.AutoField(primary_key=True)
    DIrow = models.CharField(max_length=100000)
