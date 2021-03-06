from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, \
    Founders, Filiations, Representations, Managements, Volumes, Vacs, Leaders, Teachers, FilialLeaders, \
    Leaderstwo, StandartCopies, PaidServices, Internationaldog, Internationalaccr, SpecCab, SpecPrac, SpecLib, \
    SpecSport, SpecMeal, SpecHealth, Ovz, LinkOvz, OvzTwo, Grants, GrantInfo, Acts, Jobs, GosAccreditations, Prof, \
    InfChi, AdmissionResults, Perevod, Obraz, Practices, ScienceResults, SvedOrg, Facilities, ObjPract, Libraries, \
    Sports, Meals, Health, TableOne, TableTwo, TableThree, TableFour, TableFive, TableSix, TableSeven, \
    StandartCopiestwo, GrantInfoTwo, SvedenOne, SvedenTwo, Plat, DocA, DocB, DocC, DocD, DocE, DocF, DocG, DocH, \
    DocI, DocJ, DocK, DocL, DocM, DocN, DocO, DocP


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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
            'federal',
            'sub',
            'place',
            'fis',
            'money',
            'moneyfile',
            'plan',
            'info'
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


class StandartCopiestwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandartCopiestwo
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
            'info'
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
            'grant',
            'support',
            'hostel_info',
            'inter_info',
            'hostel_ts',
            'inter_ts',
            'hostel_ls',
            'inter_ls',
            'hostel_num',
            'inter_num',
            'hostel_inv',
            'inter_inv',
            'hostel_fd',
            'inter_fd'
        )


class GrantInfoTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantInfoTwo
        fields = (
            'id',
            'grant',
            'support',
            'hostel_info',
            'inter_info',
            'hostel_ts',
            'inter_ts',
            'hostel_ls',
            'inter_ls',
            'hostel_num',
            'inter_num',
            'hostel_inv',
            'inter_inv',
            'hostel_fd',
            'inter_fd'
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


class TableOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOne
        fields = (
            'id',
            'name',
            'link'
        )


class TableTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableTwo
        fields = (
            'id',
            'name',
            'link'
        )


class TableThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableThree
        fields = (
            'id',
            'name',
            'link'
        )


class TableFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableFour
        fields = (
            'id',
            'name',
            'link'
        )


class TableFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableFive
        fields = (
            'id',
            'name',
            'link'
        )


class TableSixSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableSix
        fields = (
            'id',
            'name',
            'link'
        )


class TableSevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableSeven
        fields = (
            'id',
            'name',
            'link'
        )


class SvedenOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SvedenOne
        fields = (
            'id',
            'date_create',
            'address',
            'mode',
            'phones',
            'emails'
        )


class SvedenTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SvedenTwo
        fields = (
            'id',
            'number',
            'address_place'
        )


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = (
            'id',
            'info'
        )


class DocASerializer(serializers.ModelSerializer):
    class Meta:
        model = DocA
        fields = (
            'id',
            'document'
        )


class DocBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocB
        fields = (
            'id',
            'document'
        )


class DocCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocC
        fields = (
            'id',
            'document'
        )


class DocDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocD
        fields = (
            'id',
            'document'
        )


class DocESerializer(serializers.ModelSerializer):
    class Meta:
        model = DocE
        fields = (
            'id',
            'document'
        )


class DocFSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocF
        fields = (
            'id',
            'document'
        )


class DocGSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocG
        fields = (
            'id',
            'document'
        )


class DocHSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocH
        fields = (
            'id',
            'document'
        )


class DocISerializer(serializers.ModelSerializer):
    class Meta:
        model = DocI
        fields = (
            'id',
            'document'
        )


class DocJSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocJ
        fields = (
            'id',
            'document'
        )


class DocKSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocK
        fields = (
            'id',
            'document'
        )


class DocLSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocL
        fields = (
            'id',
            'document'
        )


class DocMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocM
        fields = (
            'id',
            'document'
        )


class DocNSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocN
        fields = (
            'id',
            'document'
        )


class DocOSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocO
        fields = (
            'id',
            'document'
        )


class DocPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocP
        fields = (
            'id',
            'document'
        )
