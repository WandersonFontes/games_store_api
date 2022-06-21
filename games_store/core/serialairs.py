from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Games


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = [
            'name', 
            'price', 
            'picture', 
            'page',
        ]