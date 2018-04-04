# Generated by Django 2.1.dev20180309075957 on 2018-03-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(blank=True, db_column='SNO', null=True, unique=True)),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=25, null=True)),
                ('nodeid', models.IntegerField(db_column='NODEID')),
                ('light', models.IntegerField(blank=True, null=True)),
                ('temp', models.IntegerField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'asdf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorHtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(blank=True, db_column='SNO', null=True, unique=True)),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=25, null=True)),
                ('nodeid', models.IntegerField(db_column='NODEID')),
                ('humidity', models.IntegerField(blank=True, db_column='Humidity', null=True)),
                ('temp', models.IntegerField(blank=True, db_column='TEMP', null=True)),
                ('pressure', models.IntegerField(blank=True, db_column='Pressure', null=True)),
            ],
            options={
                'db_table': 'Sensor_HTP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorTl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(blank=True, db_column='SNO', null=True, unique=True)),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=25, null=True)),
                ('nodeid', models.IntegerField(db_column='NODEID')),
                ('light', models.TextField(blank=True, db_column='LIGHT', null=True)),
                ('temp', models.TextField(blank=True, db_column='TEMP', null=True)),
            ],
            options={
                'db_table': 'Sensor_TL',
                'managed': False,
            },
        ),
    ]