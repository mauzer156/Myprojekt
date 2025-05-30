from rest_framework import serializers
from .models import CabinetClickLog

class CabinetClickLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabinetClickLog
        fields = ['login', 'action']


