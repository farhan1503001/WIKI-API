from django.db.models import fields
from rest_framework import serializers
from .models import Movies
class MovieSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'