# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acts(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acts'


class AdmissionResults(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    studyform = models.CharField(blank=True, null=True)
    budgetfederal = models.CharField(blank=True, null=True)
    budgetrus = models.CharField(blank=True, null=True)
    budgetplace = models.CharField(blank=True, null=True)
    budgetfiz = models.CharField(blank=True, null=True)
    summ = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission_results'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True)
    value = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AvalFacilities(models.Model):
    types = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    square = models.CharField(blank=True, null=True)
    sits = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aval_facilities'


class BasicInformations(models.Model):
    date_create = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    mode = models.CharField(blank=True, null=True)
    phones = models.CharField(blank=True, null=True)
    faxes = models.CharField(blank=True, null=True)
    emails = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    address_place = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_informations'


class Db2(models.Model):
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    specialty = models.TextField(blank=True, null=True)  # This field type is a guess.
    special_premises = models.TextField(blank=True, null=True)  # This field type is a guess.
    equipment = models.TextField(blank=True, null=True)  # This field type is a guess.
    fitness = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    owner = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'db (2)'


class EduIformations(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    studyform = models.CharField(blank=True, null=True)
    edupr = models.CharField(db_column='eduPr', blank=True, null=True)  # Field name made lowercase.
    adedupr = models.CharField(db_column='adeduPr', blank=True, null=True)  # Field name made lowercase.
    opmain = models.CharField(db_column='opMain', blank=True, null=True)  # Field name made lowercase.
    adopmain = models.CharField(db_column='adOpMain', blank=True, null=True)  # Field name made lowercase.
    educationplan = models.CharField(db_column='educationPlan', blank=True, null=True)  # Field name made lowercase.
    adeducationplan = models.CharField(db_column='adEducationPlan', blank=True, null=True)  # Field name made lowercase.
    educationannotation = models.CharField(db_column='educationAnnotation', blank=True, null=True)  # Field name made lowercase.
    adeducationannotation = models.CharField(db_column='adEducationAnnotation', blank=True, null=True)  # Field name made lowercase.
    educationshedule = models.CharField(db_column='educationShedule', blank=True, null=True)  # Field name made lowercase.
    adeducationshedule = models.CharField(db_column='adEducationShedule', blank=True, null=True)  # Field name made lowercase.
    methodology = models.CharField(blank=True, null=True)
    admethodology = models.CharField(db_column='adMethodology', blank=True, null=True)  # Field name made lowercase.
    eduel = models.CharField(db_column='eduEl', blank=True, null=True)  # Field name made lowercase.
    adeduel = models.CharField(db_column='adEduEl', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'edu_iformations'


class EduInformations(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    studyform = models.CharField(blank=True, null=True)
    edupr = models.CharField(db_column='eduPr', blank=True, null=True)  # Field name made lowercase.
    adedupr = models.CharField(db_column='adeduPr', blank=True, null=True)  # Field name made lowercase.
    opmain = models.CharField(db_column='opMain', blank=True, null=True)  # Field name made lowercase.
    adopmain = models.CharField(db_column='adopMain', blank=True, null=True)  # Field name made lowercase.
    educationplan = models.CharField(db_column='educationPlan', blank=True, null=True)  # Field name made lowercase.
    adeducationplan = models.CharField(db_column='adeducationPlan', blank=True, null=True)  # Field name made lowercase.
    educationannotation = models.CharField(db_column='educationAnnotation', blank=True, null=True)  # Field name made lowercase.
    adeducationannotation = models.CharField(db_column='adeducationAnnotation', blank=True, null=True)  # Field name made lowercase.
    educationshedule = models.CharField(db_column='educationShedule', blank=True, null=True)  # Field name made lowercase.
    adeducationshedule = models.CharField(db_column='adeducationShedule', blank=True, null=True)  # Field name made lowercase.
    methodology = models.CharField(blank=True, null=True)
    admethodology = models.CharField(blank=True, null=True)
    eduel = models.CharField(db_column='eduEl', blank=True, null=True)  # Field name made lowercase.
    adeduel = models.CharField(db_column='adeduEl', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    profile = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_informations'


class ElRes(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'el_res'


class ElRezOvzs(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'el_rez_ovzs'


class Extras(models.Model):
    kind = models.CharField(blank=True, null=True)
    mathelp = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extras'


class Facilities(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    specialty = models.CharField(blank=True, null=True)
    special_premises = models.CharField(blank=True, null=True)
    equipment = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facilities'


class Federals(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'federals'


class FilialLeaders(models.Model):
    name = models.CharField(blank=True, null=True)
    fio = models.CharField(blank=True, null=True)
    post = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filial_leaders'


class Filiations(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    off_site = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    work_time = models.CharField(blank=True, null=True)
    telephone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    website = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filiations'


class Founders(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    phones = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    off_site = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'founders'


class GosAccreditations(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    expdate = models.CharField(blank=True, null=True)
    language = models.CharField(blank=True, null=True)
    trainterm = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    column = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gos_accreditations'


class GrantInfo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    grant = models.CharField(blank=True, null=True)
    support = models.CharField(blank=True, null=True)
    hostel_info = models.CharField(blank=True, null=True)
    inter_info = models.CharField(blank=True, null=True)
    hostel_ts = models.CharField(blank=True, null=True)
    inter_ts = models.CharField(blank=True, null=True)
    hostel_ls = models.CharField(blank=True, null=True)
    inter_ls = models.CharField(blank=True, null=True)
    hostel_num = models.CharField(blank=True, null=True)
    inter_num = models.CharField(blank=True, null=True)
    hostel_inv = models.CharField(blank=True, null=True)
    inter_inv = models.CharField(blank=True, null=True)
    hostel_fd = models.CharField(blank=True, null=True)
    inter_fd = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grant_info'


class Grants(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grants'


class InfChi(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    form = models.CharField(blank=True, null=True)
    number_bf = models.CharField(blank=True, null=True)
    number_br = models.CharField(blank=True, null=True)
    number_bm = models.CharField(blank=True, null=True)
    number_p = models.CharField(blank=True, null=True)
    number_f = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_chi'


class InfSystems(models.Model):
    exist = models.CharField(blank=True, null=True)
    pc = models.CharField(blank=True, null=True)
    ebs = models.CharField(blank=True, null=True)
    elres = models.CharField(blank=True, null=True)
    asideelres = models.CharField(blank=True, null=True)
    bd = models.CharField(blank=True, null=True)
    tv = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_systems'


class Internationalaccr(models.Model):
    edu_code = models.CharField(blank=True, null=True)
    edu_name = models.CharField(blank=True, null=True)
    org_name = models.CharField(blank=True, null=True)
    date_end = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internationalAccr'


class Internationaldog(models.Model):
    state_name = models.CharField(blank=True, null=True)
    org_name = models.CharField(blank=True, null=True)
    dog_reg = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internationalDog'


class Invalides(models.Model):
    info = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invalides'


class Jobs(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    numgrad = models.CharField(blank=True, null=True)
    numworkgrad = models.CharField(blank=True, null=True)
    numgrad1 = models.CharField(blank=True, null=True)
    numworkgrad1 = models.CharField(blank=True, null=True)
    numgrad2 = models.CharField(blank=True, null=True)
    numworkgrad2 = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Leaders(models.Model):
    fio = models.CharField(blank=True, null=True)
    post = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaders'


class Leaderstwo(models.Model):
    fio = models.CharField(blank=True, null=True)
    post = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leadersTwo'


class Libraries(models.Model):
    types = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    square = models.CharField(blank=True, null=True)
    sits = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libraries'


class LinkOvz(models.Model):
    link_ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name_link = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_ovz'


class Managements(models.Model):
    name = models.CharField(blank=True, null=True)
    fio = models.CharField(blank=True, null=True)
    regulation = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managements'


class Meals(models.Model):
    types = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    square = models.CharField(blank=True, null=True)
    sits = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meals'


class Ovz(models.Model):
    facil_ovz = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    net_ovz = models.CharField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ovz'


class OvzTwo(models.Model):
    tech = models.CharField(blank=True, null=True)
    hostel_inter = models.CharField(blank=True, null=True)
    hostel_num = models.CharField(blank=True, null=True)
    inter = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ovz_two'


class PaidServices(models.Model):
    info = models.CharField(blank=True, null=True)
    dogpaid = models.CharField(blank=True, null=True)
    doc = models.CharField(blank=True, null=True)
    order = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    docnew = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paid_services'


class Practices(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    year = models.CharField(blank=True, null=True)
    profile = models.CharField(blank=True, null=True)
    studyforms = models.CharField(blank=True, null=True)
    learn = models.CharField(blank=True, null=True)
    production = models.CharField(blank=True, null=True)
    beforediplom = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'practices'


class Prof(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    name_accr = models.CharField(blank=True, null=True)
    time = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prof'


class Refugees(models.Model):
    num = models.CharField(blank=True, null=True)
    allsquare = models.CharField(blank=True, null=True)
    livesuare = models.CharField(blank=True, null=True)
    numplaces = models.CharField(blank=True, null=True)
    stock = models.CharField(blank=True, null=True)
    food = models.CharField(blank=True, null=True)
    info = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refugees'


class RefugeesOvzs(models.Model):
    num = models.CharField(blank=True, null=True)
    allsquare = models.CharField(blank=True, null=True)
    livesuare = models.CharField(blank=True, null=True)
    numplaces = models.CharField(blank=True, null=True)
    stock = models.CharField(blank=True, null=True)
    food = models.CharField(blank=True, null=True)
    info = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refugees_ovzs'


class Representations(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    work_time = models.CharField(blank=True, null=True)
    telephone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    website = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representations'


class RoomNums(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    specialty = models.CharField(blank=True, null=True)
    special_premises = models.CharField(blank=True, null=True)
    equipment = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_nums'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class ScienceResults(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    listdirections = models.CharField(blank=True, null=True)
    information = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    npr = models.CharField(blank=True, null=True)
    numstudents = models.CharField(blank=True, null=True)
    nummono = models.CharField(blank=True, null=True)
    numvac = models.CharField(blank=True, null=True)
    numforeign = models.CharField(blank=True, null=True)
    numlastrus = models.CharField(blank=True, null=True)
    numlastforeign = models.CharField(blank=True, null=True)
    patentrus = models.CharField(blank=True, null=True)
    patentforeign = models.CharField(blank=True, null=True)
    numsvidrus = models.CharField(blank=True, null=True)
    numsvidforeign = models.CharField(blank=True, null=True)
    volume = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'science_results'


class Sections(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'


class SpecCab(models.Model):
    address = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    osn = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_cab'


class SpecHealth(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    sq = models.CharField(blank=True, null=True)
    cnt = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_health'


class SpecLib(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    sq = models.CharField(blank=True, null=True)
    cnt = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_lib'


class SpecMeal(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    sq = models.CharField(blank=True, null=True)
    cnt = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_meal'


class SpecPrac(models.Model):
    address = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    osn = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_prac'


class SpecSport(models.Model):
    name = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    sq = models.CharField(blank=True, null=True)
    cnt = models.CharField(blank=True, null=True)
    ovz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_sport'


class Sports(models.Model):
    types = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    square = models.CharField(blank=True, null=True)
    sits = models.CharField(blank=True, null=True)
    fitness = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports'


class StandartCopies(models.Model):
    filename = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standart_copies'


class StudentNumbers(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    studyform = models.CharField(blank=True, null=True)
    budgetfederal = models.CharField(blank=True, null=True)
    budgetrus = models.CharField(blank=True, null=True)
    budgetplace = models.CharField(blank=True, null=True)
    budgetfiz = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_numbers'


class SubSections(models.Model):
    name = models.CharField(blank=True, null=True)
    section_id = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_sections'


class Subdivisions(models.Model):
    name = models.CharField(blank=True, null=True)
    fio = models.CharField(blank=True, null=True)
    position = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    off_site = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    file_url = models.BinaryField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdivisions'


class Teachers(models.Model):
    fio = models.CharField(blank=True, null=True)
    post = models.CharField(blank=True, null=True)
    dicipline = models.CharField(blank=True, null=True)
    edulevel = models.CharField(blank=True, null=True)
    qual = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    tittitle = models.CharField(blank=True, null=True)
    naimnapr = models.CharField(blank=True, null=True)
    levelup = models.CharField(blank=True, null=True)
    allyears = models.CharField(blank=True, null=True)
    scpecyears = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'


class TransferResults(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    studyform = models.CharField(blank=True, null=True)
    countin = models.CharField(blank=True, null=True)
    countout = models.CharField(blank=True, null=True)
    countrecover = models.CharField(blank=True, null=True)
    countexpel = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer_results'


class Transfers(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'


class UniverdocCats(models.Model):
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'univerdoc_cats'


class Univerdocs(models.Model):
    file_url = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cat_id = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'univerdocs'


class Users(models.Model):
    email = models.CharField(unique=True)
    encrypted_password = models.CharField()
    reset_password_token = models.CharField(unique=True, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(blank=True, null=True)
    last_sign_in_ip = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fio = models.CharField()
    sections = models.CharField(blank=True, null=True)
    sub_sections = models.CharField(blank=True, null=True)
    adm_sub_sections = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vacs(models.Model):
    code = models.CharField(blank=True, null=True)
    spec = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    kurs = models.CharField(blank=True, null=True)
    form = models.CharField(blank=True, null=True)
    federal = models.CharField(blank=True, null=True)
    sub = models.CharField(blank=True, null=True)
    place = models.CharField(blank=True, null=True)
    fis = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacs'


class VacsDefolt(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    spec = models.CharField(blank=True, null=True)
    level = models.CharField(blank=True, null=True)
    kurs = models.CharField(blank=True, null=True)
    form = models.CharField(blank=True, null=True)
    federal = models.CharField(blank=True, null=True)
    sub = models.CharField(blank=True, null=True)
    place = models.CharField(blank=True, null=True)
    fis = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacs_defolt'


class Volumes(models.Model):
    federal = models.CharField(blank=True, null=True)
    sub = models.CharField(blank=True, null=True)
    place = models.CharField(blank=True, null=True)
    fis = models.CharField(blank=True, null=True)
    money = models.CharField(blank=True, null=True)
    moneyfile = models.CharField(blank=True, null=True)
    plan = models.CharField(blank=True, null=True)
    info = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volumes'


class YearVolumes(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    year = models.CharField(blank=True, null=True)
    profile = models.CharField(blank=True, null=True)
    volume = models.CharField(blank=True, null=True)
    fulltime = models.CharField(blank=True, null=True)
    correspondence = models.CharField(blank=True, null=True)
    extramural = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'year_volumes'


class Years(models.Model):
    code = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    year = models.CharField(blank=True, null=True)
    profile = models.CharField(blank=True, null=True)
    studyforms = models.CharField(blank=True, null=True)
    volume = models.CharField(blank=True, null=True)
    fulltime = models.CharField(blank=True, null=True)
    internally = models.CharField(blank=True, null=True)
    extramural = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'years'
