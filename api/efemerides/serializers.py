from rest_framework import serializers
from efemerides.models import Efemerides

__author__ = 'rmoreyra'

class EfemeridesSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Efemerides
        fields = (
            'msj_efem', 'date_efem',
        )
        read_only_fields = (
            'msj_efem', 'date_efem',
        )

    def get_latest(self, obj):
        latest = obj.get_latest(obj.msj_efem)
        return latest.id if latest else None
