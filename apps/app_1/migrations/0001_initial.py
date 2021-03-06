# Generated by Django 3.2.8 on 2021-10-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainInfo',
            fields=[
                ('update_by', models.CharField(db_column='update_by', default='请输入修改者名字', max_length=32, null=True, verbose_name='修改者')),
                ('create_by', models.CharField(db_column='create_by', default='请输入创建者名字', max_length=32, verbose_name='创建者')),
                ('create_time', models.DateTimeField(db_column='create_time', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time', null=True, verbose_name='修改时间')),
                ('delete_mark', models.SmallIntegerField(db_column='delete_mark', default=0, help_text='逻辑删除键')),
                ('domain_id', models.AutoField(db_column='domain_id', help_text='域id', primary_key=True, serialize=False)),
                ('domian_name', models.CharField(db_column='domian_name', help_text='域名称', max_length=32)),
                ('domian_admin', models.CharField(db_column='domian_admin', help_text='域管理员', max_length=32, null=True)),
                ('domian_detail', models.CharField(db_column='domian_detail', help_text='域详情', max_length=3332, null=True)),
            ],
            options={
                'verbose_name': '域接口列表',
                'verbose_name_plural': '域接口列表',
                'db_table': 'domain_info',
            },
        ),
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_by', models.CharField(db_column='update_by', default='请输入修改者名字', max_length=32, null=True, verbose_name='修改者')),
                ('create_by', models.CharField(db_column='create_by', default='请输入创建者名字', max_length=32, verbose_name='创建者')),
                ('create_time', models.DateTimeField(db_column='create_time', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time', null=True, verbose_name='修改时间')),
                ('delete_mark', models.SmallIntegerField(db_column='delete_mark', default=0, help_text='逻辑删除键')),
                ('app_id', models.IntegerField(db_column='app_id', help_text='app_id')),
                ('domain_id_belonged', models.CharField(db_column='domain_id_belonged', help_text='所属域id', max_length=32)),
                ('app_type', models.CharField(db_column='app_type', help_text='app_type', max_length=32, null=True)),
                ('app_status', models.CharField(db_column='app_status', help_text='app_status', max_length=3332, null=True)),
            ],
            options={
                'db_table': 'app_info',
                'unique_together': {('app_id', 'domain_id_belonged')},
            },
        ),
    ]
