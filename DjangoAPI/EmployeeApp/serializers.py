from rest_framework import serializers

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, \
    Founders, Filiations, Representations, Managements, Volumes, Vacs, Leaders, Teachers, FilialLeaders, \
    Leaderstwo, StandartCopies, PaidServices, Internationaldog, Internationalaccr, SpecCab, SpecPrac, SpecLib, \
    SpecSport, SpecMeal, SpecHealth, Ovz, LinkOvz, OvzTwo, Grants, GrantInfo, Acts, Jobs, GosAccreditations, Prof, \
    InfChi, AdmissionResults, Perevod, Obraz, Practices, ScienceResults, SvedOrg, Facilities, ObjPract, Libraries, \
    Sports, Meals, Health


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


class InternationaldogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internationaldog
        fields = (
            'id',
            'state_name',
            'org_name',
            'dog_reg'
        )


class InternationalaccrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internationalaccr
        fields = (
            'id',
            'edu_code',
            'edu_name',
            'org_name',
            'date_end'
        )


class SpecCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecCab
        fields = (
            'id',
            'address',
            'name',
            'osn',
            'ovz'
        )


class SpecPracSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecPrac
        fields = (
            'id',
            'address',
            'name',
            'osn',
            'ovz'
        )


class SpecLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecLib
        fields = (
            'id',
            'name',
            'address',
            'sq',
            'cnt',
            'ovz'
        )


class SpecSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecSport
        fields = (
            'id',
            'name',
            'address',
            'sq',
            'cnt',
            'ovz'
        )


class SpecMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecMeal
        fields = (
            'id',
            'name',
            'address',
            'sq',
            'cnt',
            'ovz'
        )


class SpecHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecHealth
        fields = (
            'id',
            'name',
            'address',
            'sq',
            'cnt',
            'ovz'
        )


class OvzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ovz
        fields = (
            'id',
            'facil_ovz',
            'ovz',
            'net_ovz'
        )


class LinkOvzSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkOvz
        fields = (
            'id',
            'link_ovz',
            'name_link'
        )


class OvzTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvzTwo
        fields = (
            'id',
            'tech',
            'hostel_inter',
            'hostel_num',
            'inter'
        )


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grants
        fields = (
            'id',
            'filename'
        )


class GrantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantInfo
        fields = (
            'id',
            'name',
            'text'
        )


class ActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acts
        fields = (
            'id',
            'filename'
        )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = (
            'id',
            'code',
            'name',
            'numgrad',
            'numworkgrad',
            'numgrad1',
            'numworkgrad1',
            'numgrad2',
            'numworkgrad2'
        )


class GosAccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GosAccreditations
        fields = (
            'id',
            'code',
            'name',
            'level',
            'expdate',
            'language',
            'trainterm',
            'column'
        )


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = (
            'id',
            'code',
            'name',
            'name_accr',
            'time'
        )


class InfChiSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfChi
        fields = (
            'id',
            'code',
            'name',
            'level',
            'form',
            'number_bf',
            'number_br',
            'number_bm',
            'number_p',
            'number_f'
        )


class AdmissionResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionResults
        fields = (
            'id',
            'code',
            'name',
            'level',
            'studyform',
            'budgetfederal',
            'budgetrus',
            'budgetplace',
            'budgetfiz',
            'summ'
        )


class PerevodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perevod
        fields = (
            'id',
            'code',
            'name',
            'level',
            'form',
            'out',
            'to',
            'res',
            'exp'
        )


class ObrazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obraz
        fields = (
            'id',
            'code',
            'name',
            'level',
            'form',
            'main',
            'plan',
            'annot',
            'shed',
            'method',
            'pr',
            'el'
        )


class PracticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practices
        fields = (
            'id',
            'code',
            'name',
            'profile',
            'studyforms',
            'opis_obraz',
            'uch_plan',
            'annot_link',
            'calend_link',
            'norm_doc',
            'inf_pract',
            'inf_isp'
        )


class ScienceResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceResults
        fields = (
            'id',
            'code',
            'name',
            'level',
            'listdirections',
            'result_nir',
            'information'
        )


class SvedOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SvedOrg
        fields = (
            'id',
            'number',
            'address'
        )


class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = (
            'id',
            'address',
            'special_premises',
            'equipment'
        )


class ObjPractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjPract
        fields = (
            'id',
            'name',
            'address',
            'pract'
        )


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libraries
        fields = (
            'id',
            'types',
            'address',
            'square',
            'sits'
        )


class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = (
            'id',
            'types',
            'address',
            'square',
            'sits'
        )


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = (
            'id',
            'types',
            'address',
            'square',
            'sits'
        )


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = (
            'id',
            'types',
            'address',
            'square',
            'sits'
        )