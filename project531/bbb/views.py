from django.shortcuts import render

from .models import (
    TrainingMax
)

def tm(request):
    tms = TrainingMax.objects.all()
    tm = TrainingMax.objects.first()
    data = {
        'tms': tms,
        'tm': tm
    }
    return render(request, 'bbb/index.html', data)

