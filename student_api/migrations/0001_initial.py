# Generated by Django 4.1.1 on 2022-11-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('s_uname', models.CharField(max_length=25)),
                ('s_gender', models.CharField(max_length=10)),
                ('s_dob', models.CharField(max_length=20)),
                ('s_password', models.CharField(max_length=10)),
                ('s_address', models.CharField(max_length=60)),
            ],
        ),
    ]
