from rest_framework import viewsets, serializers, pagination, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from contrib.serializers import PrefixedModelSerializer

from ..models import Level, Answer


class LevelAnswerSerializer(PrefixedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'order', 'is_correct')

    @classmethod
    def parse_multi_formdata(cls, prefix, data, section):
        items_length = int(data.get(prefix + 'items_length', 0))
        updated_items = []
        instances = [str(i) for i in section.items.all().values_list('id', flat=True)]
        errors = [None] * items_length
        valid = True

        for i in range(items_length):
            subprefix = prefix + 'item[' + str(i) + '].'
            id = data.get(subprefix + 'id', None)
            errors[i] = {}
            if id in instances:
                updated_items.append(id)
                item_instance = section.items.get(id=id)
                serializer = cls(item_instance, prefix=subprefix, data=data)
                try:
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                except ValidationError as e:
                    errors[i] = e.detail
                    valid = False
            else:
                serializer = cls(prefix=subprefix, data=data)
                try:
                    serializer.is_valid(raise_exception=True)
                    serializer.save(id=None, section_id=section.id)
                except ValidationError as e:
                    errors[i] = e.detail
                    valid = False

        inst_to_del = [i for i in instances if i not in updated_items]
        section.items.filter(id__in=inst_to_del).delete()
        return errors, valid


class LevelSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = '__all__'

    def get_answers(self, instance):
        answers = instance.answers.all().order_by('order')
        return LevelAnswerSerializer(answers, many=True, context={'request': self.context['request']}).data


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['level', 'number']
    permission_classes = (AllowAny,)


    # def update(self, request, pk, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = LevelSerializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
    #
    # def destroy(self, pk):
    #     room = Level.objects.filter(id=pk)
    #     if room:
    #         room.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
