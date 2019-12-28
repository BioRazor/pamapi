from rest_framework import serializers

from pamapi.administration.models import Bussines_unit


class Bussines_unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bussines_unit
        fields = '__all__'