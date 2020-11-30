# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class EmployeeappBasicinformations(models.Model):
#     biid = models.AutoField(db_column='BIid', primary_key=True)  # Field name made lowercase.
#     biregdate = models.DateField(db_column='BIregDate')  # Field name made lowercase.
#     biaddress = models.CharField(db_column='BIaddress', max_length=1000)  # Field name made lowercase.
#     biworktime = models.CharField(db_column='BIworkTime', max_length=1000)  # Field name made lowercase.
#     bitelephone = models.CharField(db_column='BItelephone', max_length=1000)  # Field name made lowercase.
#     bifaxes = models.CharField(db_column='BIfaxes', max_length=1000)  # Field name made lowercase.
#     biemail = models.CharField(db_column='BIemail', max_length=1000)  # Field name made lowercase.
#     biaddressplace = models.CharField(db_column='BIaddressPlace', max_length=1000)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EmployeeApp_basicinformations'
#
#
# class EmployeeappDepartments(models.Model):
#     departmentid = models.AutoField(db_column='DepartmentId', primary_key=True)  # Field name made lowercase.
#     departmentname = models.CharField(db_column='DepartmentName', max_length=100)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EmployeeApp_departments'
#
#
# class EmployeeappDepartmentsinformation(models.Model):
#     diid = models.AutoField(db_column='DIid', primary_key=True)  # Field name made lowercase.
#     dirow = models.CharField(db_column='DIrow', max_length=100000)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EmployeeApp_departmentsinformation'
#
#
# class EmployeeappEmployees(models.Model):
#     employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
#     employeename = models.CharField(db_column='EmployeeName', max_length=100)  # Field name made lowercase.
#     department = models.CharField(db_column='Department', max_length=100)  # Field name made lowercase.
#     dateofjoining = models.DateField(db_column='DateOfJoining')  # Field name made lowercase.
#     photofilename = models.CharField(db_column='PhotoFileName', max_length=100)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EmployeeApp_employees'
#
#
# class Acts(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
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
#         managed = False
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
#         managed = False
#         db_table = 'ar_internal_metadata'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
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
#         managed = False
#         db_table = 'aval_facilities'
#
#
# class BasicInformations(models.Model):
#     regdate = models.CharField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(blank=True, null=True)
#     worktime = models.CharField(db_column='workTime', blank=True, null=True)  # Field name made lowercase.
#     telephone = models.CharField(blank=True, null=True)
#     emails = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#     addressplace = models.BinaryField(db_column='addressPlace', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'basic_informations'
#
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
#         managed = False
#         db_table = 'db (2)'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_flag = models.PositiveSmallIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
#         db_table = 'filial_leaders'
#
#
# class Filiations(models.Model):
#     name = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     off_site = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'filiations'
#
#
# class Founders(models.Model):
#     name = models.CharField(blank=True, null=True)
#     director = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     phones = models.CharField(blank=True, null=True)
#     email = models.CharField(blank=True, null=True)
#     off_site = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'founders'
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
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
#         managed = False
#         db_table = 'jobs'
#
#
# class Leaders(models.Model):
#     fio = models.CharField(blank=True, null=True)
#     post = models.CharField(blank=True, null=True)
#     phone = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'leaders'
#
#
# class Libraries(models.Model):
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
#         managed = False
#         db_table = 'libraries'
#
#
# class Managements(models.Model):
#     name = models.CharField(blank=True, null=True)
#     fio = models.CharField(blank=True, null=True)
#     regulation = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'managements'
#
#
# class Meals(models.Model):
#     types = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     square = models.CharField(blank=True, null=True)
#     sits = models.CharField(blank=True, null=True)
#     fitness = models.CharField(blank=True, null=True)
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'meals'
#
#
# class PaidServices(models.Model):
#     info = models.CharField(blank=True, null=True)
#     dogpaid = models.CharField(blank=True, null=True)
#     doc = models.CharField(blank=True, null=True)
#     order = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'paid_services'
#
#
# class Practices(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     year = models.CharField(blank=True, null=True)
#     profile = models.CharField(blank=True, null=True)
#     studyforms = models.CharField(blank=True, null=True)
#     learn = models.CharField(blank=True, null=True)
#     production = models.CharField(blank=True, null=True)
#     beforediplom = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'practices'
#
#
# class Refugees(models.Model):
#     num = models.CharField(blank=True, null=True)
#     allsquare = models.CharField(blank=True, null=True)
#     livesuare = models.CharField(blank=True, null=True)
#     numplaces = models.CharField(blank=True, null=True)
#     stock = models.CharField(blank=True, null=True)
#     food = models.CharField(blank=True, null=True)
#     info = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'refugees'
#
#
# class RefugeesOvzs(models.Model):
#     num = models.CharField(blank=True, null=True)
#     allsquare = models.CharField(blank=True, null=True)
#     livesuare = models.CharField(blank=True, null=True)
#     numplaces = models.CharField(blank=True, null=True)
#     stock = models.CharField(blank=True, null=True)
#     food = models.CharField(blank=True, null=True)
#     info = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'refugees_ovzs'
#
#
# class RoomNums(models.Model):
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
#         managed = False
#         db_table = 'room_nums'
#
#
# class SchemaMigrations(models.Model):
#     version = models.CharField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'schema_migrations'
#
#
# class ScienceResults(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     listdirections = models.CharField(blank=True, null=True)
#     information = models.CharField(blank=True, null=True)
#     title = models.CharField(blank=True, null=True)
#     npr = models.CharField(blank=True, null=True)
#     numstudents = models.CharField(blank=True, null=True)
#     nummono = models.CharField(blank=True, null=True)
#     numvac = models.CharField(blank=True, null=True)
#     numforeign = models.CharField(blank=True, null=True)
#     numlastrus = models.CharField(blank=True, null=True)
#     numlastforeign = models.CharField(blank=True, null=True)
#     patentrus = models.CharField(blank=True, null=True)
#     patentforeign = models.CharField(blank=True, null=True)
#     numsvidrus = models.CharField(blank=True, null=True)
#     numsvidforeign = models.CharField(blank=True, null=True)
#     volume = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'science_results'
#
#
# class Sections(models.Model):
#     name = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sections'
#
#
# class Sports(models.Model):
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
#         managed = False
#         db_table = 'sports'
#
#
# class StandartCopies(models.Model):
#     filename = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'standart_copies'
#
#
# class StudentNumbers(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     studyform = models.CharField(blank=True, null=True)
#     budgetfederal = models.CharField(blank=True, null=True)
#     budgetrus = models.CharField(blank=True, null=True)
#     budgetplace = models.CharField(blank=True, null=True)
#     budgetfiz = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'student_numbers'
#
#
# class SubSections(models.Model):
#     name = models.CharField(blank=True, null=True)
#     section_id = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     number = models.CharField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sub_sections'
#
#
# class Subdivisions(models.Model):
#     name = models.CharField(blank=True, null=True)
#     fio = models.CharField(blank=True, null=True)
#     position = models.CharField(blank=True, null=True)
#     address = models.CharField(blank=True, null=True)
#     off_site = models.CharField(blank=True, null=True)
#     email = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     file_url = models.BinaryField(blank=True, null=True)
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'subdivisions'
#
#
# class Teachers(models.Model):
#     fio = models.CharField(blank=True, null=True)
#     post = models.CharField(blank=True, null=True)
#     dicipline = models.CharField(blank=True, null=True)
#     edulevel = models.CharField(blank=True, null=True)
#     qual = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     tittitle = models.CharField(blank=True, null=True)
#     naimnapr = models.CharField(blank=True, null=True)
#     levelup = models.CharField(blank=True, null=True)
#     allyears = models.CharField(blank=True, null=True)
#     scpecyears = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'teachers'
#
#
# class TransferResults(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     studyform = models.CharField(blank=True, null=True)
#     countin = models.CharField(blank=True, null=True)
#     countout = models.CharField(blank=True, null=True)
#     countrecover = models.CharField(blank=True, null=True)
#     countexpel = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'transfer_results'
#
#
# class Transfers(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
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
#         managed = False
#         db_table = 'univerdoc_cats'
#
#
# class Univerdocs(models.Model):
#     file_url = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     cat_id = models.IntegerField(blank=True, null=True)
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'univerdocs'
#
#
# class Users(models.Model):
#     email = models.CharField(unique=True)
#     encrypted_password = models.CharField()
#     reset_password_token = models.CharField(unique=True, blank=True, null=True)
#     reset_password_sent_at = models.DateTimeField(blank=True, null=True)
#     remember_created_at = models.DateTimeField(blank=True, null=True)
#     sign_in_count = models.IntegerField()
#     current_sign_in_at = models.DateTimeField(blank=True, null=True)
#     last_sign_in_at = models.DateTimeField(blank=True, null=True)
#     current_sign_in_ip = models.CharField(blank=True, null=True)
#     last_sign_in_ip = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     fio = models.CharField()
#     sections = models.CharField(blank=True, null=True)
#     sub_sections = models.CharField(blank=True, null=True)
#     adm_sub_sections = models.CharField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#
#
# class Vacs(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     spec = models.CharField(blank=True, null=True)
#     level = models.CharField(blank=True, null=True)
#     kurs = models.CharField(blank=True, null=True)
#     form = models.CharField(blank=True, null=True)
#     federal = models.CharField(blank=True, null=True)
#     sub = models.CharField(blank=True, null=True)
#     place = models.CharField(blank=True, null=True)
#     fis = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'vacs'
#
#
# class Volumes(models.Model):
#     federal = models.CharField(blank=True, null=True)
#     sub = models.CharField(blank=True, null=True)
#     place = models.CharField(blank=True, null=True)
#     fis = models.CharField(blank=True, null=True)
#     money = models.CharField(blank=True, null=True)
#     moneyfile = models.CharField(blank=True, null=True)
#     plan = models.CharField(blank=True, null=True)
#     info = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'volumes'
#
#
# class YearVolumes(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     year = models.CharField(blank=True, null=True)
#     profile = models.CharField(blank=True, null=True)
#     volume = models.CharField(blank=True, null=True)
#     fulltime = models.CharField(blank=True, null=True)
#     correspondence = models.CharField(blank=True, null=True)
#     extramural = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'year_volumes'
#
#
# class Years(models.Model):
#     code = models.CharField(blank=True, null=True)
#     name = models.CharField(blank=True, null=True)
#     year = models.CharField(blank=True, null=True)
#     profile = models.CharField(blank=True, null=True)
#     studyforms = models.CharField(blank=True, null=True)
#     volume = models.CharField(blank=True, null=True)
#     fulltime = models.CharField(blank=True, null=True)
#     internally = models.CharField(blank=True, null=True)
#     extramural = models.CharField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     owner = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'years'
