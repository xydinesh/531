from rest_framework import serializers
from .models import (
    BbbUser,
    Tm,
    TmData,
    Cycle
)

class TmDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TmData
        fields = ("id", "name", "lift", "weight", "date")

class CycleSerializer(serializers.ModelSerializer)        :

    class Meta:
        model = Cycle
        fields = ("id", "lift", "weight", "date", "cycle", "tm")
