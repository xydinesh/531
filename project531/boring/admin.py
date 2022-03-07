from django.contrib import admin
from .models import (
    Tm,
    Cycle
)
# Register your models here.
admin.site.register(Tm)
admin.site.register(Cycle)
