# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Acts(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'acts'
#
#
# class AdmissionResults(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     studyform = models.CharField(blank=True, null=True)
#     budgetfederal = models.CharField(blank=True, null=True)
#     budgetrus = models.CharField(blank=True, null=True)
#     budgetplace = models.CharField(blank=True, null=True)
#     budgetfiz = models.CharField(blank=True, null=True)
#     summ = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'admission_results'
#
#
# class ArInternalMetadata(models.Model):
#     key = models.CharField(primary_key=True)
#     value = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#
#         db_table = 'ar_internal_metadata'
#
#
# class AvalFacilities(models.Model):
#     types = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     square = models.CharField(blank=True, null=True)
#     sits = models.CharField(blank=True, null=True)
#     fitness = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'aval_facilities'
#

class BasicInformations(models.Model):
    date_create = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    mode = models.CharField(blank=True, null=True, max_length=1000)
    phones = models.CharField(blank=True, null=True, max_length=1000)
    faxes = models.CharField(blank=True, null=True, max_length=1000)
    emails = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    address_place = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'basic_informations'


#
# class Db2(models.Model):
#     code = models.TextField(blank=True, null=True)  # This field type is a guess.
#     name = models.TextField(blank=True, null=True)  # This field type is a guess.
#     specialty = models.TextField(blank=True, null=True)  # This field type is a guess.
#     special_premises = models.TextField(blank=True, null=True)  # This field type is a guess.
#     equipment = models.TextField(blank=True, null=True)  # This field type is a guess.
#     fitness = models.TextField(blank=True, null=True)  # This field type is a guess.
#     created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
#     updated_at = models.TextField(blank=True, null=True)  # This field type is a guess.
#     owner = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#
#         db_table = 'db (2)'
#
#
# class EduIformations(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     studyform = models.CharField(blank=True, null=True)
#     edupr = models.CharField(db_column='eduPr', blank=True, null=True)  # Field name made lowercase.
#     adedupr = models.CharField(db_column='adeduPr', blank=True, null=True)  # Field name made lowercase.
#     opmain = models.CharField(db_column='opMain', blank=True, null=True)  # Field name made lowercase.
#     adopmain = models.CharField(db_column='adOpMain', blank=True, null=True)  # Field name made lowercase.
#     educationplan = models.CharField(db_column='educationPlan', blank=True, null=True)  # Field name made lowercase.
#     adeducationplan = models.CharField(db_column='adEducationPlan', blank=True, null=True)  # Field name made lowercase.
#     educationannotation = models.CharField(db_column='educationAnnotation', blank=True, null=True)  # Field name made lowercase.
#     adeducationannotation = models.CharField(db_column='adEducationAnnotation', blank=True, null=True)  # Field name made lowercase.
#     educationshedule = models.CharField(db_column='educationShedule', blank=True, null=True)  # Field name made lowercase.
#     adeducationshedule = models.CharField(db_column='adEducationShedule', blank=True, null=True)  # Field name made lowercase.
#     methodology = models.CharField(blank=True, null=True)
#     admethodology = models.CharField(db_column='adMethodology', blank=True, null=True)  # Field name made lowercase.
#     eduel = models.CharField(db_column='eduEl', blank=True, null=True)  # Field name made lowercase.
#     adeduel = models.CharField(db_column='adEduEl', blank=True, null=True)  # Field name made lowercase.
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#
#         db_table = 'edu_iformations'
#
#
# class EduInformations(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     studyform = models.CharField(blank=True, null=True)
#     edupr = models.CharField(db_column='eduPr', blank=True, null=True)  # Field name made lowercase.
#     adedupr = models.CharField(db_column='adeduPr', blank=True, null=True)  # Field name made lowercase.
#     opmain = models.CharField(db_column='opMain', blank=True, null=True)  # Field name made lowercase.
#     adopmain = models.CharField(db_column='adopMain', blank=True, null=True)  # Field name made lowercase.
#     educationplan = models.CharField(db_column='educationPlan', blank=True, null=True)  # Field name made lowercase.
#     adeducationplan = models.CharField(db_column='adeducationPlan', blank=True, null=True)  # Field name made lowercase.
#     educationannotation = models.CharField(db_column='educationAnnotation', blank=True, null=True)  # Field name made lowercase.
#     adeducationannotation = models.CharField(db_column='adeducationAnnotation', blank=True, null=True)  # Field name made lowercase.
#     educationshedule = models.CharField(db_column='educationShedule', blank=True, null=True)  # Field name made lowercase.
#     adeducationshedule = models.CharField(db_column='adeducationShedule', blank=True, null=True)  # Field name made lowercase.
#     methodology = models.CharField(blank=True, null=True)
#     admethodology = models.CharField(blank=True, null=True)
#     eduel = models.CharField(db_column='eduEl', blank=True, null=True)  # Field name made lowercase.
#     adeduel = models.CharField(db_column='adeduEl', blank=True, null=True)  # Field name made lowercase.
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#     profile = models.CharField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'edu_informations'
#
#
# class ElRes(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'el_res'
#
#
# class ElRezOvzs(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'el_rez_ovzs'
#
#
# class Extras(models.Model):
#     kind = models.CharField(blank=True, null=True)
#     mathelp = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'extras'
#
#
# class Facilities(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     specialty = models.CharField(blank=True, null=True)
#     special_premises = models.CharField(blank=True, null=True)
#     equipment = models.CharField(blank=True, null=True)
#     fitness = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'facilities'
#
#
# class Federals(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'federals'
#
#
# class FilialLeaders(models.Model):
#     name = models.CharField(blank=True, null=True)
#     fio = models.CharField(blank=True, null=True)
#     post = models.CharField(blank=True, null=True)
#     phone = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'filial_leaders'
#
#
class Filiations(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    off_site = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True, max_length=1000)
    work_time = models.CharField(blank=True, null=True, max_length=1000)
    telephone = models.CharField(blank=True, null=True, max_length=1000)
    email = models.CharField(blank=True, null=True, max_length=1000)
    website = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'filiations'


#
#

class Founders(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    phones = models.CharField(blank=True, null=True, max_length=1000)
    email = models.CharField(blank=True, null=True, max_length=1000)
    off_site = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'founders'


class Representations(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    work_time = models.CharField(blank=True, null=True, max_length=1000)
    telephone = models.CharField(blank=True, null=True, max_length=1000)
    email = models.CharField(blank=True, null=True, max_length=1000)
    website = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'representations'


#
#
# class GosAccreditations(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     expdate = models.CharField(blank=True, null=True)
#     language = models.CharField(blank=True, null=True)
#     trainterm = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'gos_accreditations'
#
#
# class Grants(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'grants'
#
#
# class InfSystems(models.Model):
#     exist = models.CharField(blank=True, null=True)
#     pc = models.CharField(blank=True, null=True)
#     ebs = models.CharField(blank=True, null=True)
#     elres = models.CharField(blank=True, null=True)
#     asideelres = models.CharField(blank=True, null=True)
#     bd = models.CharField(blank=True, null=True)
#     tv = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'inf_systems'
#
#
# class Invalides(models.Model):
#     info = models.CharField(blank=True, null=True)
#     ovz = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'invalides'
#
#
# class Jobs(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     numgrad = models.CharField(blank=True, null=True)
#     numworkgrad = models.CharField(blank=True, null=True)
#     numgrad1 = models.CharField(blank=True, null=True)
#     numworkgrad1 = models.CharField(blank=True, null=True)
#     numgrad2 = models.CharField(blank=True, null=True)
#     numworkgrad2 = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'jobs'
#
#
class Leaders(models.Model):
    fio = models.CharField(blank=True, null=True, max_length=1000)
    post = models.CharField(blank=True, null=True, max_length=1000)
    phone = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'leaders'
#
#
# class Libraries(models.Model):
#     types = models.CharField(blank=True, null=True, max_length=100)
#     address = models.CharField(blank=True, null=True, max_length=100)
#     square = models.CharField(blank=True, null=True, max_length=100)
#     sits = models.CharField(blank=True, null=True, max_length=100)
#     fitness = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'libraries'
#
#
class Managements(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    fio = models.CharField(blank=True, null=True, max_length=1000)
    regulation = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'managements'


#
#
# class Meals(models.Model):
#     types = models.CharField(blank=True, null=True, max_length=100)
#     address = models.CharField(blank=True, null=True, max_length=100)
#     square = models.CharField(blank=True, null=True, max_length=100)
#     sits = models.CharField(blank=True, null=True, max_length=100)
#     fitness = models.CharField(blank=True, null=True, max_length=100)
#     filename = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'meals'
#
#
# class PaidServices(models.Model):
#     info = models.CharField(blank=True, null=True, max_length=100)
#     dogpaid = models.CharField(blank=True, null=True, max_length=100)
#     doc = models.CharField(blank=True, null=True, max_length=100)
#     order = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'paid_services'
#
#
# class Practices(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     year = models.CharField(blank=True, null=True, max_length=100)
#     profile = models.CharField(blank=True, null=True, max_length=100)
#     studyforms = models.CharField(blank=True, null=True, max_length=100)
#     learn = models.CharField(blank=True, null=True, max_length=100)
#     production = models.CharField(blank=True, null=True, max_length=100)
#     beforediplom = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'practices'
#
#
# class Refugees(models.Model):
#     num = models.CharField(blank=True, null=True, max_length=100)
#     allsquare = models.CharField(blank=True, null=True, max_length=100)
#     livesuare = models.CharField(blank=True, null=True, max_length=100)
#     numplaces = models.CharField(blank=True, null=True, max_length=100)
#     stock = models.CharField(blank=True, null=True, max_length=100)
#     food = models.CharField(blank=True, null=True, max_length=100)
#     info = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'refugees'
#
#
# class RefugeesOvzs(models.Model):
#     num = models.CharField(blank=True, null=True, max_length=100)
#     allsquare = models.CharField(blank=True, null=True, max_length=100)
#     livesuare = models.CharField(blank=True, null=True, max_length=100)
#     numplaces = models.CharField(blank=True, null=True, max_length=100)
#     stock = models.CharField(blank=True, null=True, max_length=100)
#     food = models.CharField(blank=True, null=True, max_length=100)
#     info = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'refugees_ovzs'
#
#
# class RoomNums(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     specialty = models.CharField(blank=True, null=True, max_length=100)
#     special_premises = models.CharField(blank=True, null=True, max_length=100)
#     equipment = models.CharField(blank=True, null=True, max_length=100)
#     fitness = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'room_nums'
#
#
# class SchemaMigrations(models.Model):
#     version = models.CharField(primary_key=True, max_length=100)
#
#     class Meta:
#
#         db_table = 'schema_migrations'
#
#
# class ScienceResults(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     listdirections = models.CharField(blank=True, null=True, max_length=100)
#     information = models.CharField(blank=True, null=True, max_length=100)
#     title = models.CharField(blank=True, null=True, max_length=100)
#     npr = models.CharField(blank=True, null=True, max_length=100)
#     numstudents = models.CharField(blank=True, null=True, max_length=100)
#     nummono = models.CharField(blank=True, null=True, max_length=100)
#     numvac = models.CharField(blank=True, null=True, max_length=100)
#     numforeign = models.CharField(blank=True, null=True, max_length=100)
#     numlastrus = models.CharField(blank=True, null=True, max_length=100)
#     numlastforeign = models.CharField(blank=True, null=True, max_length=100)
#     patentrus = models.CharField(blank=True, null=True, max_length=100)
#     patentforeign = models.CharField(blank=True, null=True, max_length=100)
#     numsvidrus = models.CharField(blank=True, null=True, max_length=100)
#     numsvidforeign = models.CharField(blank=True, null=True, max_length=100)
#     volume = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'science_results'
#
#
# class Sections(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'sections'
#
#
# class Sports(models.Model):
#     types = models.CharField(blank=True, null=True, max_length=100)
#     address = models.CharField(blank=True, null=True, max_length=100)
#     square = models.CharField(blank=True, null=True, max_length=100)
#     sits = models.CharField(blank=True, null=True, max_length=100)
#     fitness = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'sports'
#
#
# class StandartCopies(models.Model):
#     filename = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True, max_length=100)
#
#     class Meta:
#
#         db_table = 'standart_copies'
#
#
# class StudentNumbers(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     level = models.CharField(blank=True, null=True, max_length=100)
#     studyform = models.CharField(blank=True, null=True, max_length=100)
#     budgetfederal = models.CharField(blank=True, null=True, max_length=100)
#     budgetrus = models.CharField(blank=True, null=True, max_length=100)
#     budgetplace = models.CharField(blank=True, null=True, max_length=100)
#     budgetfiz = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'student_numbers'
#
#
# class SubSections(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=100)
#     section_id = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     number = models.CharField(blank=True, null=True, max_length=100)
#
#     class Meta:
#
#         db_table = 'sub_sections'


class Subdivisions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    fio = models.CharField(blank=True, null=True, max_length=1000)
    position = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    off_site = models.CharField(blank=True, null=True, max_length=1000)
    email = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    file_url = models.CharField(blank=True, null=True, max_length=1000)
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'subdivisions'


#
# class Teachers(models.Model):
#     fio = models.CharField(blank=True, null=True, max_length=100)
#     post = models.CharField(blank=True, null=True, max_length=100)
#     dicipline = models.CharField(blank=True, null=True, max_length=100)
#     edulevel = models.CharField(blank=True, null=True, max_length=100)
#     qual = models.CharField(blank=True, null=True, max_length=100)
#     level = models.CharField(blank=True, null=True, max_length=100)
#     tittitle = models.CharField(blank=True, null=True, max_length=100)
#     naimnapr = models.CharField(blank=True, null=True, max_length=100)
#     levelup = models.CharField(blank=True, null=True, max_length=100)
#     allyears = models.CharField(blank=True, null=True, max_length=100)
#     scpecyears = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'teachers'
#
#
# class TransferResults(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     level = models.CharField(blank=True, null=True, max_length=100)
#     studyform = models.CharField(blank=True, null=True, max_length=100)
#     countin = models.CharField(blank=True, null=True, max_length=100)
#     countout = models.CharField(blank=True, null=True, max_length=100)
#     countrecover = models.CharField(blank=True, null=True, max_length=100)
#     countexpel = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'transfer_results'
#
#
# class Transfers(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'transfers'
#
#
# class UniverdocCats(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'univerdoc_cats'
#
#
# class Univerdocs(models.Model):
#     file_url = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     cat_id = models.IntegerField(blank=True, null=True)
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'univerdocs'
#
#
# class Users(models.Model):
#     email = models.CharField(unique=True)
#     encrypted_password = models.CharField()
#     reset_password_token = models.CharField(unique=True, blank=True, null=True, max_length=100)
#     reset_password_sent_at = models.DateTimeField(blank=True, null=True)
#     remember_created_at = models.DateTimeField(blank=True, null=True)
#     sign_in_count = models.IntegerField()
#     current_sign_in_at = models.DateTimeField(blank=True, null=True)
#     last_sign_in_at = models.DateTimeField(blank=True, null=True)
#     current_sign_in_ip = models.CharField(blank=True, null=True, max_length=100)
#     last_sign_in_ip = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     fio = models.CharField(max_length=100)
#     sections = models.CharField(blank=True, null=True, max_length=100)
#     sub_sections = models.CharField(blank=True, null=True, max_length=100)
#     adm_sub_sections = models.CharField(blank=True, null=True, max_length=100)
#
#     class Meta:
#
#         db_table = 'users'
#
#
class Vacs(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    spec = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    kurs = models.CharField(blank=True, null=True, max_length=1000)
    form = models.CharField(blank=True, null=True, max_length=1000)
    federal = models.CharField(blank=True, null=True, max_length=1000)
    sub = models.CharField(blank=True, null=True, max_length=1000)
    place = models.CharField(blank=True, null=True, max_length=1000)
    fis = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'vacs'


#
#
class Volumes(models.Model):
    federal = models.CharField(blank=True, null=True, max_length=1000)
    sub = models.CharField(blank=True, null=True, max_length=1000)
    place = models.CharField(blank=True, null=True, max_length=1000)
    fis = models.CharField(blank=True, null=True, max_length=1000)
    money = models.CharField(blank=True, null=True, max_length=1000)
    moneyfile = models.CharField(blank=True, null=True, max_length=1000)
    plan = models.CharField(blank=True, null=True, max_length=1000)
    info = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'volumes'


#
#
# class YearVolumes(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     year = models.CharField(blank=True, null=True, max_length=100)
#     profile = models.CharField(blank=True, null=True, max_length=100)
#     volume = models.CharField(blank=True, null=True, max_length=100)
#     fulltime = models.CharField(blank=True, null=True, max_length=100)
#     correspondence = models.CharField(blank=True, null=True, max_length=100)
#     extramural = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'year_volumes'
#
#
# class Years(models.Model):
#     code = models.CharField(blank=True, null=True, max_length=100)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     year = models.CharField(blank=True, null=True, max_length=100)
#     profile = models.CharField(blank=True, null=True, max_length=100)
#     studyforms = models.CharField(blank=True, null=True, max_length=100)
#     volume = models.CharField(blank=True, null=True, max_length=100)
#     fulltime = models.CharField(blank=True, null=True, max_length=100)
#     internally = models.CharField(blank=True, null=True, max_length=100)
#     extramural = models.CharField(blank=True, null=True, max_length=100)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'years'


# Old models

# from django.db import models


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


# class BasicInformations(models.Model):
#     BIid = models.AutoField(primary_key=True)
#     BIregDate = models.DateField()
#     BIaddress = models.CharField(max_length=1000)
#     BIworkTime = models.CharField(max_length=1000)
#     BItelephone = models.CharField(max_length=1000)
#     BIfaxes = models.CharField(max_length=1000)
#     BIemail = models.CharField(max_length=1000)
#     BIaddressPlace = models.CharField(max_length=1000)


class DepartmentsInformation(models.Model):
    DIid = models.AutoField(primary_key=True)
    DIrow = models.CharField(max_length=100000)
