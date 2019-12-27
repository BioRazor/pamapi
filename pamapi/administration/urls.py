# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

from .views import bussines_unit as bussines_unitViews



router = DefaultRouter()
router.register(r'bussines_unit', bussines_unitViews.Bussines_unitViewSet, basename='bussines_unit')
urlpatterns = [
    path('', include(router.urls))
]