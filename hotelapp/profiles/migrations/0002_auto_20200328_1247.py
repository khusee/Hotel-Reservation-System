# Generated by Django 2.2 on 2020-03-28 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 12, 47, 45, 22443)),
        ),
    ]
