from django.db import models
from django.utils.timezone import now

# Create your models here.

# 公共抽象类


class BaseModel(models.Model):

    # 修改者
    AppFilter = models.CharField(
        db_column="update_by", 
        max_length=32,
        verbose_name="AppFilter",
        null=True,
        default="daiyi")

    # 创建者
    create_by = models.CharField(
        db_column="create_by", max_length=32,
        verbose_name="create_by",
        null=True,
        default="daiyi")

    # 创建时间
    create_time = models.DateTimeField(
        db_column="create_time",
        null=True,)

    # 修改时间
    update_time = models.DateTimeField(
        db_column="update_time",
        auto_now=True,
        blank=True,
        null=True)

    # 软删除
    delete_mark = models.SmallIntegerField(
        default=0, db_column='delete_mark', help_text="delete_mark")

    class Meta:
        abstract = True


class DomainInfo(BaseModel):
    domain_id = models.AutoField(
        db_column='domain_id', help_text='domain_id', primary_key=True)
    domian_name = models.CharField(
        db_column='domian_name', help_text="domian_name", max_length=32)
    domian_admin = models.CharField(
        db_column='domian_admin', help_text="domian_admin", max_length=32, null=True)
    domian_detail = models.CharField(
        db_column='domian_detail', help_text="domian_detail",
        null=True, max_length=3332)

    class Meta:
        db_table = 'domain_info'
        # 设置表名，默认表名是：应用名称_模型类名
        # 带有应用名的表名太长了
        verbose_name = 'domain_api_list'
        verbose_name_plural = "domain_api_list"

    def __str__(self):
        return "domain_model_class"


class AppInfo(BaseModel):
    app_id = models.IntegerField(
        db_column='app_id', help_text='app_id')
    domain_id_belonged = models.CharField(
        db_column='domain_id_belonged', help_text="domain_id_belonged", max_length=32)
    app_type = models.CharField(
        db_column='app_type', help_text="app_type", max_length=32, null=True)
    app_status = models.CharField(
        db_column='app_status', help_text="app_status",
        null=True, max_length=3332)

    class Meta:
        db_table = 'app_info'
        unique_together = (("app_id", "domain_id_belonged"),)

    def __str__(self):
        return "app_model_class"


class OperationInfo(BaseModel):
    op_id = models.AutoField(
        db_column='op_id', help_text='op_id', primary_key=True)
    op_user = models.CharField(
        db_column='op_user', help_text="op_user", max_length=323, null=True)
    
    op_type = models.CharField(
        db_column='op_type', help_text="op_type", max_length=32, null=True)
    op_res = models.CharField(
        db_column='op_res', help_text="op_res",
        null=True, max_length=3332)

    class Meta:
        db_table = 'op_info'

    def __str__(self):
        return "op_model_class"
