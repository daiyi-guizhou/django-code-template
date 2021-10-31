"""django_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .apps.app_1.views.domain import DomainSet
from .apps.app_1.views.app import AppSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="测试工程API",
        default_version='v1.0',
        description="测试工程接口文档",
        terms_of_service="https://www.cnblogs.com/jinjiangongzuoshi/",
        contact=openapi.Contact(email="daiyi"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r"^app/", AppSet)
router.register(r"^domain/", DomainSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置 前端 路由 (vue 静态文件)
    path('front/', TemplateView.as_view(template_name='index.html'), name='index'),

    # 配置django-rest-framwork API路由
    # path('sso/', include('..apps.sso.urls')),
    path(r'^api/', include(router.urls)),
    # path('app_1/', include('..apps.app_1.urls')),

    # 配置drf-yasg路由
    path('^swagger(?P<format>\.json|\.yaml)$',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
