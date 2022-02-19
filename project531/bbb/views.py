from django.shortcuts import render

from .models import (
    TrainingMax
)

def tm(request):
    tm = TrainingMax.objects.first()
    data = {
        'tm': tm,
    }
    return render(request, 'bbb/index.html', data)

