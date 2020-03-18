from rest_framework import viewsets, serializers, pagination, status
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter

from ..models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [SearchFilter]
    permission_classes = (AllowAny,)
