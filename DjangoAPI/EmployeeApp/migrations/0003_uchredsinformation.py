# Generated by Django 3.1.3 on 2020-11-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_departmentsinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UchredsInformation',
            fields=[
                ('UBIid', models.AutoField(primary_key=True, serialize=False)),
                ('UBIrow', models.CharField(max_length=100000)),
            ],
        ),
    ]