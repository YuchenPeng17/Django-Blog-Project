"""
URL configuration for django_project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    
    # www.xxx.com/index/ -> app01 views里的index函数
	path("index/", views.index),

    path("users/list/", views.user_list),

    path("users/add/", views.user_add),

    # 模版语法
    path("tpl/", views.tpl),

    # 请求与响应
    path("something/", views.something),

    # 案例：用户登陆
    path("login/", views.login),

    # ORM
    path("orm/", views.orm),

]
