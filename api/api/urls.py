"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from efemerides.views import (EfemeridesViewSet)
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.decorators import login_required

__author__ = 'rmoreyra'

router = routers.DefaultRouter()
router.register(r'api', EfemeridesViewSet, base_name='efemerides')

schema_view = get_swagger_view(title='REST API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('efemerides.urls')),
    url(r'^swagger/?', login_required(schema_view)),
]
