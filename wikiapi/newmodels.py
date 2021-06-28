# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    index = models.IntegerField(db_column='index',blank=True, null=True)
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
    average_rating = models.TextField(db_column='Average Rating', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_count = models.TextField(db_column='User Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    genres = models.TextField(db_column='Genres', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'movies'
