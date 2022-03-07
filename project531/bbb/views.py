from django.shortcuts import render

from .models import (
    TrainingMax
)

def tm(request):
    tms = TrainingMax.objects.all().order_by('-record_date')
    tm = TrainingMax.objects.first()
    data = {
        'tms': tms,
        'tm': tm
    }
    return render(request, 'bbb/index.html', data)

