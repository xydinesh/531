from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TmViewSet,
    CycleViewSet
)

router = DefaultRouter()
router.register(r'tms', TmViewSet)
router.register(r'cycles', CycleViewSet)

urlpatterns = [
    path("", include(router.urls))
]
