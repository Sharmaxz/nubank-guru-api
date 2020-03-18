from rest_framework import viewsets, serializers, pagination, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from contrib.serializers import PrefixedModelSerializer

from ..models import Level


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['level', 'position']
    permission_classes = (AllowAny,)