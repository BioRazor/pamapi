from rest_framework import viewsets

from pamapi.administration.models import Bussines_unit
from pamapi.administration.serializers import Bussines_unitSerializer

class Bussines_unitViewSet(viewsets.ModelViewSet):
    queryset = Bussines_unit.objects.all()
    serializer_class = Bussines_unitSerializer