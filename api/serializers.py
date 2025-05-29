from rest_framework import serializers
from .models import ClickLog

class ClickLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickLog
        fields = ['log_entry']
