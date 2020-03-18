from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer


class PrefixedModelSerializer(ModelSerializer):
    def __init__(self, instance=None, data=empty, prefix='', **kwargs):
        self.prefix = prefix
        new_data = data
        if data is not empty:
            new_data = {}
            for k, v in data.items():
                if prefix in k:
                    new_data[k[len(prefix):]] = v
        super().__init__(instance=instance, data=new_data, **kwargs)
