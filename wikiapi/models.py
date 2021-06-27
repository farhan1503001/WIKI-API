# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Movies(models.Model):
    index = models.IntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    directed_by = models.TextField(db_column='Directed by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    produced_by = models.TextField(db_column='Produced by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    screenplay_by = models.TextField(db_column='Screenplay by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    based_on = models.TextField(db_column='Based on', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starring = models.TextField(db_column='Starring', blank=True, null=True)  # Field name made lowercase.
    music_by = models.TextField(db_column='Music by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cinematography = models.TextField(db_column='Cinematography', blank=True, null=True)  # Field name made lowercase.
    edited_by = models.TextField(db_column='Edited by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    productioncompanies_field = models.TextField(db_column='Productioncompanies ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    distributed_by = models.TextField(db_column='Distributed by', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    release_date = models.TextField(db_column='Release date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    running_time = models.TextField(db_column='Running time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    budget = models.TextField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.
    box_office = models.TextField(db_column='Box office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'movies'
