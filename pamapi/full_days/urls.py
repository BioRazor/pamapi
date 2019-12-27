# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
# from .views import circles as circle_views
# from .views import memberships as membership_views

router = DefaultRouter()
# router.register(r'full_days', circle_views.CircleViewSet, basename='circle')
urlpatterns = [
    path('', include(router.urls))
]