from rest_framework import serializers

from .models import BasicInformations, Subdivisions


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = ('DepartmentId',
#                   'DepartmentName')
#
#
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employees
#         fields = ('EmployeeId',
#                   'EmployeeName',
#                   'Department',
#                   'DateOfJoining',
#                   'PhotoFileName')
#
#
# class BasicInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BasicInformations
#         fields = ('BIid',
#                   'BIregDate',
#                   'BIaddress',
#                   'BIworkTime',
#                   'BItelephone',
#                   'BIfaxes',
#                   'BIemail',
#                   'BIaddressPlace')
#
#
# class DepartmentsInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DepartmentsInformation
#         fields = (
#             'DIid',
#             'DIrow'
#         )


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
            'regDate',
            'address',
            'workTime',
            'telephone',
            'email',
            'addressPlace'
        )
