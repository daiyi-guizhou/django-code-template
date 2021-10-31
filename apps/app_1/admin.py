from django.contrib import admin

# Register your models here.

from .models import DomainInfo
admin.site.register(DomainInfo)
