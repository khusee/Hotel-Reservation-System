# Generated by Django 2.2 on 2020-03-28 07:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('tv_service', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('attached_bathroom', models.BooleanField()),
                ('air_conditioner', models.BooleanField()),
                ('key_card', models.BooleanField()),
                ('wifi_service', models.BooleanField()),
                ('room_service', models.BooleanField()),
                ('total_rooms', models.IntegerField(default=5)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_one', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_two', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_three', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('agents', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomType', models.CharField(max_length=255)),
                ('capacity', models.IntegerField(default=1)),
                ('TotalRooms', models.IntegerField()),
                ('price', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
            ],
        ),
    ]
