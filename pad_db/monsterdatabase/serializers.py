from rest_framework import serializers

from .models import Monster


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'
