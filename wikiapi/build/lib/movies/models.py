from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.IntegerField(db_column='index',blank=True, null=False,primary_key=True)
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
        db_table = 'movies'
