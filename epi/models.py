# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Data(models.Model):
    """This class represents the data model."""
    name = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True, related_name="children")
    data_source = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='data', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'data'

    def __str__(self):
        return self.name


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
