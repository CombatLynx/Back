from rest_framework import serializers

from .models import Departments, Employees, BasicInformations, DepartmentsInformation


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')


class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformations
        fields = ('BIid',
                  'BIregDate',
                  'BIaddress',
                  'BIworkTime',
                  'BItelephone',
                  'BIfaxes',
                  'BIemail',
                  'BIaddressPlace')


class UchredBISerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentsInformation
        fields = (
            'UBIid',
            'UBIrow'
        )


class DepartmentsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentsInformation
        fields = (
            'DIid',
            'DIrow'
        )
