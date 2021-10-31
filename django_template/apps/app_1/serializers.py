import django_filters
from rest_framework import serializers

from .models import (DomainInfo, AppInfo)


class BaseSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(
        input_formats=['%Y-%n-%d %H:%M:%S'],
        format='%Y-%n-%d %H:%M:%S', required=False)
    update_time = serializers.DateTimeField(
        input_formats=['%Y-%n-%d %H:%M:%S'],
        format='%Y-%n-%d %H:%M:%S', required=False)


class DomainSerializer(BaseSerializer):
    class Meta:
        model = DomainInfo
        fields = "__all__"

    def validate_name(self, value):
        """
        局部验证
        """
        return value


class AppSerializer(BaseSerializer):
    class Meta:
        model = AppInfo
        fields = "__all__"

# filters
# https://blog.csdn.net/linux_player_c/article/details/80779059
# https://blog.csdn.net/weixin_42935779/article/details/105863728
# field_name（必选）：模型类的属性
# lookup_expr（可选）：判断条件

# iexact：表示精确匹配, 并且忽略大小写
# icontains：表示模糊查询（包含），并且忽略大小写
# exact：表示精确匹配
# gte：用于规定范围，大于等于
# lte： 用于范围，小于等于
# method： 自己定义一个方法
# help_text： 帮助说明


class AppFilter(django_filters.rest_framework.FilterSet):
    domain_id_belonged = django_filters.NumberFilter(
        name='domain_id_belonged')

    class Meta:
        model = AppInfo
        fields = ['domain_id_belonged']


class DomainFilter(django_filters.rest_framework.FilterSet):
    domian_name = django_filters.CharFilter(
        name='domian_name', lookup_expr='icontains')
    create_by = django_filters.CharFilter(
        name='create_by', lookup_expr='icontains')
    domian_admin = django_filters.CharFilter(
        name='domian_admin', lookup_expr='icontains')
    max_time = django_filters.DateTimeFilter(
        name='create_time', lookup_expr="lte")
    min_time = django_filters.DateTimeFilter(
        name='create_time', lookup_expr="gte")

    class Meta:
        model = DomainInfo
        fields = ['domian_name', 'create_by',
                  'domian_admin', 'max_time', 'min_time', 'create_time', ]
