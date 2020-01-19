import logging
from rest_framework import (viewsets, mixins, views, permissions, status)
from rest_framework.response import Response
from efemerides.models import Efemerides
from efemerides.serializers import EfemeridesSerializer
from efemerides.constants import MONTH, CURRENT_DAY
from datetime import datetime
from django.conf import settings
import calendar
from django.http import JsonResponse

__author__ = 'rmoreyra'

logger = logging.getLogger(__name__)

class EfemeridesViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    create:
    TODO Create Efemerides.

    list:
    List Efemerides.
    """

    queryset = Efemerides.objects.all().order_by('-created')
    serializer_class = EfemeridesSerializer

    def _build_efem_month(self,list_efem_month):
        """
        Build dict with all ephemeris in month
        """
        result_data = dict()
        for efem in list_efem_month:
            datetime_efem = efem.date_efem
            result_data[str(datetime_efem.day)] = efem.msj_efem
        return result_data

    def _get_list_efem(self, date_find, date_day_of_month):
        """
        Get list ephemeris in [date_find, date_day_of_month]
        """
        list_efem = Efemerides.objects.filter(date_efem__gte=date_find, date_efem__lte=date_day_of_month).order_by(
            'date_efem')
        return list_efem

    def _get_efem(self, date_find):
        """
        Get ephemeride with date equal at date_find
        """
        return Efemerides.objects.filter(date_efem=date_find).order_by('date_efem')

    def _get_date_find(self, request):
        """
        Get str of date searched
        """
        date_find = '{} 00:00:00'.format(dict(request.query_params)['day'][0])
        return date_find

    def _get_last_date_month(self, date_find):
        """
        Get str of last date month
        """
        day = datetime.strptime(date_find, settings.TIME_FORMAT)
        last_day_of_month = calendar.monthrange(day.year, day.month)[1]
        date_day_of_month = '{}-{}-{} 00:00:00'.format(day.year, day.month, last_day_of_month)
        return date_day_of_month

    def _build_data_result(self, efem, list_efem):
        """
        Builds data of response
        """
        result_data = dict()
        result_data[CURRENT_DAY] = list(efem.values())[0]['msj_efem']
        result_data[MONTH] = dict()
        result_data[MONTH] = self._build_efem_month(list_efem)
        return result_data

    def list(self, request, *args, **kwargs):
        if not dict(request.query_params):
            queryset = Efemerides.objects.all()
            data = list(queryset.values())
            return JsonResponse(data, safe=False)
        date_find = self._get_date_find(request)
        efem = self._get_efem(date_find)
        if not list(efem.values()):
            msj_error = 'not info to {}'.format(date_find)
            return Response(
                {'error': msj_error},
                status=status.HTTP_400_BAD_REQUEST
            )
        date_day_of_month = self._get_last_date_month(date_find)

        list_efem = self._get_list_efem(date_find, date_day_of_month)

        result_data = self._build_data_result(efem, list_efem)

        return Response(
                result_data,
                status=status.HTTP_200_OK
            )

    def create(self, request):
        validation_result = request.data
        # valid_schema = self._validation_schema(validation_result)
        # if not valid_schema[0]:
        #     return Response(
        #         {'error': valid_schema[1]},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        if True:
            return Response(
                {'info': 'not implemented'},
                status=status.HTTP_501_NOT_IMPLEMENTED
                )

        str_date = '{} 00:00:00'.format(validation_result['day'])
        new_date = datetime.strptime(str_date, settings.TIME_FORMAT)
        new_product = Efemerides.objects.create(
                msj_efem=validation_result['msj'],
                date_efem=new_date
            )

        new_product_response = EfemeridesSerializer(
            new_product,
            context={'request': request}
        )

        headers = self.get_success_headers(new_product_response.data)
        return Response(
            new_product_response.data, status=cod_status, headers=headers
        )

