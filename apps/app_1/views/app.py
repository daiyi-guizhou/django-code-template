from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from .common import CommonSet
from ..models import AppInfo, DomainInfo
from ..serializers import DomainFilter, AppFilter, AppSerializer, DomainSerializer
import django_filters

from rest_framework.response import Response
from rest_framework.decorators import action


class AppSet(CommonSet):
    read_only_fileds = (
        "update_by",
        "create_by",
        "create_time",
        "update_time",
    )

    queryset = AppInfo.objects.filter()
    serializer_class = AppSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = AppFilter
    url_name = "app"
    view_name = "app"
