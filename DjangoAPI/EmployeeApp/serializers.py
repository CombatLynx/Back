from rest_framework import serializers

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, \
    Founders, Filiations, Representations, Managements, Volumes, Vacs, Leaders, Teachers, FilialLeaders, \
    Leaderstwo, StandartCopies, PaidServices


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


class VolumesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volumes
        fields = (
            'id',
            'name',
            'fio',
            'regulation'
        )


class VacsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacs
        fields = (
            'id',
            'code',
            'name',
            'spec',
            'level',
            'kurs',
            'form',
            'federal',
            'sub',
            'place',
            'fis'
        )


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaders
        fields = (
            'id',
            'fio',
            'post',
            'phone',
            'address'
        )


class LeaderstwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderstwo
        fields = (
            'id',
            'fio',
            'post',
            'phone',
            'address'
        )


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = (
            'id',
            'fio',
            'post',
            'dicipline',
            'edulevel',
            'qual',
            'level',
            'tittitle',
            'naimnapr',
            'levelup',
            'allyears',
            'scpecyears'
        )


class FilialLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialLeaders
        fields = (
            'id',
            'name',
            'fio',
            'post',
            'phone',
            'address'
        )


class StandartCopiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandartCopies
        fields = (
            'id',
            'name',
            'filename'
        )


class PaidServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidServices
        fields = (
            'id',
            'info',
            'dogpaid',
            'doc',
            'order'
        )
