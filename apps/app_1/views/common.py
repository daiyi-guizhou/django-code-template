# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from .middlerware import RequestLogView
# Django drf ViewSets
# https://www.w3cschool.cn/lxraw/lxraw-qiyu35oo.html


class CommonSet(RequestLogView, viewsets.ModelViewSet):
    read_only_fileds = (
        "update_by",
        "create_by",
        "create_time",
        "update_time",
    )
