# Generated by Django 3.0 on 2020-12-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('cpassword', models.CharField(max_length=200)),
            ],
        ),
    ]
