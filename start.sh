# 创建project
django-admin startproject django_template
cd django_template/
mkdir settings apps test 
mv settings.py settings
touch settings/__init__.py
touch apps/__init__.py
touch test/__init__.py
 
 
# python manager.py startapp <app_name> [app_directory]  # 创建app
mkdir -p apps/sso
mkdir -p apps/app_1
python manage.py startapp sso ./apps/sso
python manage.py startapp app_1 ./apps/app_1


cp django_template/settings.py settings/
mv settings/settings.py settings/base.py
touch settings/window_dev.py settings/linux_dev.py
mv settings django_template/

sed -i 's/django_template.settings/django_template.settings.window_dev/g'  manage.py

# 数据库准备
mysql -u root -p 123456;
create database daiyi_apps;

# django model 迁移
python manage.py makemigrations
python manage.py migrate


pyhton manage.py runserver  [127.0.0.1:8000]  # 启动
pyhton manage.py shell  # 调试

