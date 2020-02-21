from .models import Excursion
from rest_framework import serializers

class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields = '__all__'
