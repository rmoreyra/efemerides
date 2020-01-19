from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from efemerides.views import EfemeridesViewSet

__author__ = 'rmoreyra'

router = routers.DefaultRouter()
router.register(r'efemerides', EfemeridesViewSet, base_name='efemerides')

plan_exec_router = NestedSimpleRouter(router, r'efemerides', lookup='day')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(plan_exec_router.urls))
]
