from rest_framework import serializers

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, \
    Founders, Filiations, Representations, Managements


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


class DepartmentsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentsInformation
        fields = (
            'DIid',
            'DIrow'
        )


class SubdivisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivisions
        fields = (
            'id',
            'name',
            'fio',
            'position',
            'address',
            'off_site',
            'email',
            'file_url'
        )


class BasicInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformations
        fields = (
            'id',
            'date_create',
            'address',
            'mode',
            'phones',
            'emails',
            'address_place'
        )


class FoundersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founders
        fields = (
            'id',
            'name',
            'address',
            'phones',
            'email',
            'off_site'
        )


class FiliationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiations
        fields = (
            'id',
            'name',
            'address',
            'work_time',
            'telephone',
            'email',
            'website'
        )


class RepresentationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representations
        fields = (
            'id',
            'name',
            'address',
            'work_time',
            'telephone',
            'email',
            'website'
        )


class ManagementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managements
        fields = (
            'id',
            'name',
            'fio',
            'regulation'
        )
