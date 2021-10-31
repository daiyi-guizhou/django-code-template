
from .common import CommonSet
from ..models import AppInfo, DomainInfo
from ..serializers import DomainFilter, AppFilter, AppSerializer, DomainSerializer
import django_filters

from rest_framework.response import Response
from rest_framework.decorators import action


class DomainSet(CommonSet):
    queryset = DomainInfo.objects.filter()
    serializer_class = DomainSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = DomainFilter
    url_name = "domain"
    view_name = "domain"

    def get_queryset(self):
        return DomainInfo.objects.filter(delete_mark=0)

    # https://www.cnblogs.com/zhzhlong/p/9325180.html
    # @action()
    # action装饰器可以接收两个参数：
    # methods: 声明该action对应的请求方式，列表传递
    # detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk > /action方法名/
    # True 表示路径格式是xxx/<pk > /action方法名/
    # False 表示路径格式是xxx/action方法名/
    @action(methods=["post"], detail=True)
    def search(self, requset, *args, **kwargs):
        data = request.data
        msg = {"message": "自定义url 和actions",
               "code": 200}

        return Response(msg)
