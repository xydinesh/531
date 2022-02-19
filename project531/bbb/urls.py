from django.urls import path

from . import views

urlpatterns = [
    path('', views.tm, name='tm'),
]
