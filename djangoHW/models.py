# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
# Create your models here.


class Djangohw(models.Model):
    todo_id = models.AutoField(primary_key=True)
    completed = models.BooleanField(default=False)
    todo = models.CharField(max_length=20)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'djangohw'
