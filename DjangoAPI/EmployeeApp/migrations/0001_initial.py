# Generated by Django 3.1.3 on 2020-11-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformations',
            fields=[
                ('BIid', models.AutoField(primary_key=True, serialize=False)),
                ('BIregDate', models.DateField()),
                ('BIaddress', models.CharField(max_length=1000)),
                ('BIworkTime', models.CharField(max_length=1000)),
                ('BItelephone', models.CharField(max_length=1000)),
                ('BIfaxes', models.CharField(max_length=1000)),
                ('BIemail', models.CharField(max_length=1000)),
                ('BIaddressPlace', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
    ]
