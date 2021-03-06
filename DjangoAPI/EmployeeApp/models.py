# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class User(models.Model):
#     username = models.CharField(blank=True, null=True, max_length=1000)
#     email = models.CharField(blank=True, null=True, max_length=1000)
#     password = models.CharField(blank=True, null=True, max_length=1000)
#
#     class Meta:
#         db_table = 'user'


class Acts(models.Model):
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'acts'


class AdmissionResults(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    studyform = models.CharField(blank=True, null=True, max_length=1000)
    budgetfederal = models.CharField(blank=True, null=True, max_length=1000)
    budgetrus = models.CharField(blank=True, null=True, max_length=1000)
    budgetplace = models.CharField(blank=True, null=True, max_length=1000)
    budgetfiz = models.CharField(blank=True, null=True, max_length=1000)
    summ = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'admission_results'


class Obraz(models.Model):
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    form = models.CharField(blank=True, null=True, max_length=1000)
    main = models.CharField(blank=True, null=True, max_length=1000)
    plan = models.CharField(blank=True, null=True, max_length=1000)
    annot = models.CharField(blank=True, null=True, max_length=1000)
    shed = models.CharField(blank=True, null=True, max_length=1000)
    method = models.CharField(blank=True, null=True, max_length=1000)
    pr = models.CharField(blank=True, null=True, max_length=1000)
    el = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'obraz'


class ObjPract(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    pract = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'obj_pract'


class Perevod(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    form = models.CharField(blank=True, null=True, max_length=1000)
    out = models.CharField(blank=True, null=True, max_length=1000)
    to = models.CharField(blank=True, null=True, max_length=1000)
    res = models.CharField(blank=True, null=True, max_length=1000)
    exp = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'perevod'


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


class SpecCab(models.Model):
    address = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    osn = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_cab'


class SpecPrac(models.Model):
    address = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    osn = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_prac'


class SpecLib(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    sq = models.CharField(blank=True, null=True, max_length=1000)
    cnt = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_lib'


class SpecSport(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    sq = models.CharField(blank=True, null=True, max_length=1000)
    cnt = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_sport'


class SpecMeal(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    sq = models.CharField(blank=True, null=True, max_length=1000)
    cnt = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_meal'


class SpecHealth(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    sq = models.CharField(blank=True, null=True, max_length=1000)
    cnt = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spec_health'


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
class FilialLeaders(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    fio = models.CharField(blank=True, null=True, max_length=1000)
    post = models.CharField(blank=True, null=True, max_length=1000)
    phone = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'filial_leaders'


#
#
class Filiations(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    off_site = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
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
    owner = models.IntegerField(blank=True, null=True)

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
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'representations'


class Ovz(models.Model):
    facil_ovz = models.CharField(blank=True, null=True, max_length=1000)
    ovz = models.CharField(blank=True, null=True, max_length=1000)
    net_ovz = models.CharField(blank=True, null=True, max_length=1000)
    owner = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'ovz'


class OvzTwo(models.Model):
    tech = models.CharField(blank=True, null=True, max_length=1000)
    hostel_inter = models.CharField(blank=True, null=True, max_length=1000)
    hostel_num = models.CharField(blank=True, null=True, max_length=1000)
    inter = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ovz_two'


class LinkOvz(models.Model):
    link_ovz = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name_link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'link_ovz'


class GosAccreditations(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    expdate = models.CharField(blank=True, null=True, max_length=1000)
    language = models.CharField(blank=True, null=True, max_length=1000)
    trainterm = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    column = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'gos_accreditations'


class Prof(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    name_accr = models.CharField(blank=True, null=True, max_length=1000)
    time = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'prof'


class GrantInfo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    grant = models.CharField(blank=True, null=True, max_length=1000)
    support = models.CharField(blank=True, null=True, max_length=1000)
    hostel_info = models.CharField(blank=True, null=True, max_length=1000)
    inter_info = models.CharField(blank=True, null=True, max_length=1000)
    hostel_ts = models.CharField(blank=True, null=True, max_length=1000)
    inter_ts = models.CharField(blank=True, null=True, max_length=1000)
    hostel_ls = models.CharField(blank=True, null=True, max_length=1000)
    inter_ls = models.CharField(blank=True, null=True, max_length=1000)
    hostel_num = models.CharField(blank=True, null=True, max_length=1000)
    inter_num = models.CharField(blank=True, null=True, max_length=1000)
    hostel_inv = models.CharField(blank=True, null=True, max_length=1000)
    inter_inv = models.CharField(blank=True, null=True, max_length=1000)
    hostel_fd = models.CharField(blank=True, null=True, max_length=1000)
    inter_fd = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'grant_info'


class GrantInfoTwo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    grant = models.CharField(blank=True, null=True, max_length=1000)
    support = models.CharField(blank=True, null=True, max_length=1000)
    hostel_info = models.CharField(blank=True, null=True, max_length=1000)
    inter_info = models.CharField(blank=True, null=True, max_length=1000)
    hostel_ts = models.CharField(blank=True, null=True, max_length=1000)
    inter_ts = models.CharField(blank=True, null=True, max_length=1000)
    hostel_ls = models.CharField(blank=True, null=True, max_length=1000)
    inter_ls = models.CharField(blank=True, null=True, max_length=1000)
    hostel_num = models.CharField(blank=True, null=True, max_length=1000)
    inter_num = models.CharField(blank=True, null=True, max_length=1000)
    hostel_inv = models.CharField(blank=True, null=True, max_length=1000)
    inter_inv = models.CharField(blank=True, null=True, max_length=1000)
    hostel_fd = models.CharField(blank=True, null=True, max_length=1000)
    inter_fd = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'grant_info_two'


class Grants(models.Model):
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'grants'


class InfChi(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    form = models.CharField(blank=True, null=True, max_length=1000)
    number_bf = models.CharField(blank=True, null=True, max_length=1000)
    number_br = models.CharField(blank=True, null=True, max_length=1000)
    number_bm = models.CharField(blank=True, null=True, max_length=1000)
    number_p = models.CharField(blank=True, null=True, max_length=1000)
    number_f = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'inf_chi'


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
class Internationalaccr(models.Model):
    edu_code = models.CharField(blank=True, null=True, max_length=1000)
    edu_name = models.CharField(blank=True, null=True, max_length=1000)
    org_name = models.CharField(blank=True, null=True, max_length=1000)
    date_end = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'internationalAccr'


class Internationaldog(models.Model):
    state_name = models.CharField(blank=True, null=True, max_length=1000)
    org_name = models.CharField(blank=True, null=True, max_length=1000)
    dog_reg = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'internationalDog'


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
class Jobs(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    numgrad = models.CharField(blank=True, null=True, max_length=1000)
    numworkgrad = models.CharField(blank=True, null=True, max_length=1000)
    numgrad1 = models.CharField(blank=True, null=True, max_length=1000)
    numworkgrad1 = models.CharField(blank=True, null=True, max_length=1000)
    numgrad2 = models.CharField(blank=True, null=True, max_length=1000)
    numworkgrad2 = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'jobs'


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


class Leaderstwo(models.Model):
    fio = models.CharField(blank=True, null=True, max_length=1000)
    post = models.CharField(blank=True, null=True, max_length=1000)
    phone = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'leadersTwo'


class Libraries(models.Model):
    types = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    square = models.CharField(blank=True, null=True, max_length=1000)
    sits = models.CharField(blank=True, null=True, max_length=1000)
    fitness = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'libraries'


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


class Meals(models.Model):
    types = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    square = models.CharField(blank=True, null=True, max_length=1000)
    sits = models.CharField(blank=True, null=True, max_length=1000)
    fitness = models.CharField(blank=True, null=True, max_length=1000)
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'meals'


class Health(models.Model):
    types = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    square = models.CharField(blank=True, null=True, max_length=1000)
    sits = models.CharField(blank=True, null=True, max_length=1000)
    fitness = models.CharField(blank=True, null=True, max_length=1000)
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'health'


class SvedenOne(models.Model):
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
        db_table = 'sveden_one'


class SvedenTwo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    address_place = models.CharField(blank=True, null=True, max_length=1000)
    number = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'sveden_two'


class DocA(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_a'


class DocB(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_b'


class DocC(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_c'


class DocD(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_d'


class DocE(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_e'


class DocF(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_f'


class DocG(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_g'


class DocH(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_h'


class DocI(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_i'


class DocJ(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_j'


class DocK(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_k'


class DocL(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_l'


class DocM(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_m'


class DocN(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_n'


class DocO(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_o'


class DocP(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    document = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'doc_p'


class Plat(models.Model):
    info = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'plat'


class PaidServices(models.Model):
    info = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'paid_services'


class Practices(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    year = models.CharField(blank=True, null=True, max_length=1000)
    profile = models.CharField(blank=True, null=True, max_length=1000)
    studyforms = models.CharField(blank=True, null=True, max_length=1000)
    learn = models.CharField(blank=True, null=True, max_length=1000)
    production = models.CharField(blank=True, null=True, max_length=1000)
    beforediplom = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    opis_obraz = models.CharField(blank=True, null=True, max_length=1000)
    uch_plan = models.CharField(blank=True, null=True, max_length=1000)
    annot_link = models.CharField(blank=True, null=True, max_length=1000)
    calend_link = models.CharField(blank=True, null=True, max_length=1000)
    norm_doc = models.CharField(blank=True, null=True, max_length=1000)
    inf_pract = models.CharField(blank=True, null=True, max_length=1000)
    inf_isp = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'practices'


class TableFive(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_five'


class TableFour(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_four'


class TableOne(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_one'


class TableSeven(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_seven'


class TableSix(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_six'


class TableThree(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_three'


class TableTwo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    link = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'table_two'
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
class ScienceResults(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    listdirections = models.CharField(blank=True, null=True, max_length=1000)
    information = models.CharField(blank=True, null=True, max_length=1000)
    title = models.CharField(blank=True, null=True, max_length=1000)
    npr = models.CharField(blank=True, null=True, max_length=1000)
    numstudents = models.CharField(blank=True, null=True, max_length=1000)
    nummono = models.CharField(blank=True, null=True, max_length=1000)
    numvac = models.CharField(blank=True, null=True, max_length=1000)
    numforeign = models.CharField(blank=True, null=True, max_length=1000)
    numlastrus = models.CharField(blank=True, null=True, max_length=1000)
    numlastforeign = models.CharField(blank=True, null=True, max_length=1000)
    patentrus = models.CharField(blank=True, null=True, max_length=1000)
    patentforeign = models.CharField(blank=True, null=True, max_length=1000)
    numsvidrus = models.CharField(blank=True, null=True, max_length=1000)
    numsvidforeign = models.CharField(blank=True, null=True, max_length=1000)
    volume = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    level = models.CharField(blank=True, null=True, max_length=1000)
    result_nir = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'science_results'


class Facilities(models.Model):
    code = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(blank=True, null=True, max_length=1000)
    specialty = models.CharField(blank=True, null=True, max_length=1000)
    special_premises = models.CharField(blank=True, null=True, max_length=1000)
    equipment = models.CharField(blank=True, null=True, max_length=1000)
    fitness = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'facilities'


class SvedOrg(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    number = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'sved_org'


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
class Sports(models.Model):
    types = models.CharField(blank=True, null=True, max_length=1000)
    address = models.CharField(blank=True, null=True, max_length=1000)
    square = models.CharField(blank=True, null=True, max_length=1000)
    sits = models.CharField(blank=True, null=True, max_length=1000)
    fitness = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sports'


#
#
class StandartCopies(models.Model):
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'standart_copies'


class StandartCopiestwo(models.Model):
    filename = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'standart_copiestwo'
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


class Teachers(models.Model):
    fio = models.CharField(blank=True, null=True, max_length=1000)
    post = models.CharField(blank=True, null=True, max_length=1000)
    dicipline = models.CharField(blank=True, null=True, max_length=1000)
    edulevel = models.CharField(blank=True, null=True, max_length=1000)
    qual = models.CharField(blank=True, null=True, max_length=1000)
    level = models.CharField(blank=True, null=True, max_length=1000)
    tittitle = models.CharField(blank=True, null=True, max_length=1000)
    naimnapr = models.CharField(blank=True, null=True, max_length=1000)
    levelup = models.CharField(blank=True, null=True, max_length=1000)
    allyears = models.CharField(blank=True, null=True, max_length=1000)
    scpecyears = models.CharField(blank=True, null=True, max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'teachers'


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
#
#     class Meta:
#         db_table = 'basic_informations'


class DepartmentsInformation(models.Model):
    DIid = models.AutoField(primary_key=True)
    DIrow = models.CharField(max_length=100000)
