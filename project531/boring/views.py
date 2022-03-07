from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import (
    TmDataSerializer,
    CycleSerializer
)
from .models import (
    Tm,
    Cycle
)

class TmViewSet(viewsets.ModelViewSet):
    serializer_class = TmDataSerializer
    queryset = Tm.objects.all()

class CycleViewSet(viewsets.ModelViewSet):
    serializer_class = CycleSerializer
    queryset = Cycle.objects.all()
    
