# Generated by Django 3.2.4 on 2021-06-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('directed_by', models.TextField(blank=True, db_column='Directed by', null=True)),
                ('produced_by', models.TextField(blank=True, db_column='Produced by', null=True)),
                ('screenplay_by', models.TextField(blank=True, db_column='Screenplay by', null=True)),
                ('based_on', models.TextField(blank=True, db_column='Based on', null=True)),
                ('starring', models.TextField(blank=True, db_column='Starring', null=True)),
                ('music_by', models.TextField(blank=True, db_column='Music by', null=True)),
                ('cinematography', models.TextField(blank=True, db_column='Cinematography', null=True)),
                ('edited_by', models.TextField(blank=True, db_column='Edited by', null=True)),
                ('productioncompanies_field', models.TextField(blank=True, db_column='Productioncompanies ', null=True)),
                ('distributed_by', models.TextField(blank=True, db_column='Distributed by', null=True)),
                ('release_date', models.TextField(blank=True, db_column='Release date', null=True)),
                ('running_time', models.TextField(blank=True, db_column='Running time', null=True)),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('language', models.TextField(blank=True, db_column='Language', null=True)),
                ('budget', models.TextField(blank=True, db_column='Budget', null=True)),
                ('box_office', models.TextField(blank=True, db_column='Box office', null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
