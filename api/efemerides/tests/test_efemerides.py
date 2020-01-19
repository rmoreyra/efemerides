from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, NoReverseMatch
from efemerides.views import EfemeridesViewSet
from django.conf import settings
from datetime import datetime
from mock import patch

__author__ = 'rmoreyra'

class mock_efem(object):
    def __init__(self, date_efem, msj_efem):
        self.date_efem = datetime.strptime('{} 00:00:00'.format(date_efem), settings.TIME_FORMAT)
        self.msj_efem = msj_efem
    def values(self):
        return [{'msj_efem':self.msj_efem}]

# class mock_efem(object):
#     def values(self):
#         return [{'msj_efem':'Dia del test'}]

class EfemeridesTestCase(APITestCase):
    def setUp(self):
        self.username = 'admin'
        self.user_email = 'rmoreyra@gmail.com'
        self.user_pass = self.username + '123'
        user_defautls = {'password': make_password(self.user_pass),
                         'email': self.user_email}

        self.user, _ = User.objects.get_or_create(
            username=self.username,
            defaults=user_defautls
        )
        self.client.login(
            username=self.username,
            password=self.user_pass
        )
        self.mock_list_efem = [mock_efem('2020-01-01', 'Dia del unit test1'),
                          mock_efem('2020-01-02', 'Dia del unit test2'),
                          mock_efem('2020-01-03','Dia del unit test3')]

    def test_endpoint_exists(self):
        try:
            url=reverse('efemerides-list')
            self.assertEqual(url, '/api/efemerides/')
        except NoReverseMatch:
            self.fail('The view doesn\'t exist')

    def test_build_efem_month(self):
        efemerides = EfemeridesViewSet()
        result_data = efemerides._build_efem_month(self.mock_list_efem)
        self.assertEqual(result_data, {'1': ['Dia del unit test1'],
                                       '2': ['Dia del unit test2'],
                                       '3': ['Dia del unit test3']})

    def test_get_date_find(self):
        efemerides = EfemeridesViewSet()
        with  patch("rest_framework.request.Request") as mock_request:
            mock_request.query_params = {'day':['2020-01-10']}
            value_str_date_find = efemerides._get_date_find(mock_request)
            self.assertEqual(value_str_date_find, '2020-01-10 00:00:00')

    def test_get_invalid_day(self):
        url = reverse('efemerides-list')
        url = url + '?day=2015-25'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)
        response_body = response.json()
        self.assertEqual(response_body.get('error'), 'Invalid date format in day parameter')
        self.assertEqual(response_body.get('info'), 'Correct format is yyyy-mm-dd')

    def test_get_without_day(self):
        url = reverse('efemerides-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertEqual(response_body, [])

    def test_build_data_result(self):
        efemerides = EfemeridesViewSet()
        result_data = efemerides._build_data_result(mock_efem('2020-01-01','Dia del unit test1'),self.mock_list_efem)
        self.assertEqual(result_data, {'hoy': 'Dia del unit test1', 'mes': {'1': ['Dia del unit test1'],
                                                                            '2': ['Dia del unit test2'],
                                                                            '3': ['Dia del unit test3']}})

    def test_get_last_date_month(self):
        efemerides = EfemeridesViewSet()
        date_find = '2020-2-10 00:00:00'
        expected_value = '2020-2-29 00:00:00'
        date_day_of_month = efemerides._get_last_date_month(date_find)
        self.assertEqual(date_day_of_month, expected_value)
