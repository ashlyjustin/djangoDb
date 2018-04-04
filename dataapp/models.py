from django.db import models

# Create your models here.
from django.db import models


class SensorHtp(models.Model):
    sno = models.IntegerField(db_column='SNO', unique=True, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nodeid = models.IntegerField(db_column='NODEID')  # Field name made lowercase.
    humidity = models.IntegerField(db_column='Humidity', blank=True, null=True)  # Field name made lowercase.
    temp = models.IntegerField(db_column='TEMP', blank=True, null=True)  # Field name made lowercase.
    pressure = models.IntegerField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sensor_HTP'


class SensorTl(models.Model):

    sno = models.IntegerField(db_column='SNO', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nodeid = models.IntegerField(db_column='NODEID')  # Field name made lowercase.
    light = models.TextField(db_column='LIGHT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp = models.TextField(db_column='TEMP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Sensor_TL'


class Asdf(models.Model):
    sno = models.IntegerField(db_column='SNO', unique=True, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nodeid = models.IntegerField(db_column='NODEID')  # Field name made lowercase.
    light = models.IntegerField(blank=True, null=True)
    temp = models.IntegerField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'asdf'
