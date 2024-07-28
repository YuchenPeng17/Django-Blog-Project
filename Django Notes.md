# Day1 Basics

## 1. Start Project

```
django-admin startproject <django_project01>
```



## 2. 目录

```
django_project01
├── django_project01								
│   ├── __init__.py
│   ├── asgi.py											【接受网络请求】【不用动】
│   ├── settings.py									【项目配置文件】【常用】
│   ├── urls.py											【url和函数的对应关系】【常用】
│   └── wsgi.py											【接受网络请求】【不用动】
└── manage.py												【项目管理脚本，启动项目，创建app，数据管理】【不用动】
```



## 3. APP

```
- 项目
	- app，用户管理
	- app，订单管理
	- app，网站
	...
```

```
创建app
python manage.py startapp <app01>
```

```
├── app01
│   ├── __init__.py
│   ├── admin.py							【不用动】admin后台管理
│   ├── apps.py								【不用动】app启动类
│   ├── migrations						【不用动】数据库字段变更
│   │   └── __init__.py
│   ├── models.py							【重要】对数据操作
│   ├── tests.py							【单元测试】【不用动】
│   └── views.py							【重要】url对应的函数写在这里
...
```



## 4. 快速上手

- Step1: 确保app已经注册

```
app01:
apps.py
class App01Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app01"

project:
settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
		# 注册
		"app01.apps.App01Config",
]
```

- Step2: 编写URL和视图函数的对应关系

```
project:
urls.py

from app01 import views
urlpatterns = [
    path("admin/", admin.site.urls),
    
    # www.xxx.com/index/ -> app01 views里的index函数
		path("index/", views.index),
]
```

- Step3: 编写视图函数

```
app01:
views.py

# reques: default parameter
def index(request):
    return HttpResponse("Welcome")
```

- Step4: 启动项目

```
命令行：
python manage.py runserver
```



### 4.1 One More 页面

```
Step1: 在Project的urls.py中写好Url和函数的对应关系
Step2: 在aoo的views.py中写视图函数
```

### 4.2 Templates模版

```
def user_list(request):
    return render(request, "user_list.html")
    
默认在当前app目录下，在templates文件夹下寻找。（根据app注册顺序，逐一去templates目录下找）
```

### 4.3 Static File / 静态文件

```
- 图片
- CSS
- Js

在app目录下/在templates同级位置，创建static文件夹，存入静态文件
{% load static %}
<link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1-dist/css/bootstrap.css' %}">

...
    │   ├── static
    │   │   ├── css
    │   │   ├── img
    │   │   │   └── 1.png
    │   │   ├── js
    │   │   └── plugins
    │   ├── templates
    │   │   └── user_list.html
...


```



## 5. 模版语法

- 在HTMl中写占位符，由数据对这些占位符进行替换和处理。

views.py

```django
def tpl(request):
    name_db = "Yuchen"
    comment_db = "All Good"
    role_db = ["programmer", "developer", "data analyst"]
    user_info_db = {
        "name": "Yovan",
        "salary": 70000,
        "role": "graduate job",
    }
    data_list_db = [
        {"name": "Yovan", "salary": 70000, "role": "graduate job"},
        {"name": "Osa", "salary": 170000, "role": "junior job"},
        {"name": "Levi", "salary": 270000, "role": "senior job"}
    ]
    return render(request, "tpl.html", {
        "name": name_db,
        "comment": comment_db,
        "role": role_db,
        "user_info": user_info_db,
        "data_list": data_list_db,
    })
```

HTML

```html
<!-- 1. normal variable -->
<h3>{{ name }}</h3>
<h4>{{ comment }}</h4>
<hr>

<!-- 2. array, list -->
<ul>
{% for item in role %}
	<li>{{ item }}</li>
{% endfor %}
</ul>
<hr>

<!-- 3. object -->
<!-- user_info.keys; user_info.values; user_info.items -->
{% for key,value in user_info.items %}
	<li>{{ key }} = {{ value }}</li>
{% endfor %}
<hr>

<!-- 4. objects in array -->
<div>{{ data_list.2.name }}</div>
{% for item in data_list %}
	<div>
		<span>{{item.name}} with {{item.salary}} is {{item.role}}</span>
	</div>
{% endfor %}
<hr>

<!-- 5. conditinal statements -->
{% if name == "Yuchen" %}
	<h1>If Yes</h1>
{% elif name == "Yovan" %}
	<h1>If No Sure</h1>
{% else %}
	<h1>If No</h1>
{% endif %}
```

- Step1: 用户发来请求至urls.py
- Step2：urls.py发送请求至view.py
- Step3：view.py通过函数拿到templates中<u>带有模版语法的页面</u>
- Step4：视图函数render内部
  - 读取含有模版语法的html文件
  - 内部进行渲染（模版语法执行并替换数据）
  - 最终得到只包含html标签的字符串
- Step5：将渲染完成的字符串返还给用户的浏览器



## 6. 请求与响应

- Request是一个对象
  - 封装了用户发送来的所有请求相关数据
- Redirect：Django `redirect` 函数通过发送包含目标URL的HTTP重定向响应，指示浏览器自动访问新的URL。

```django
urls.py
# 请求与响应
path("something/", views.something),
```

```django
views.py
3中请求，3种响应
def something(request):
    # 1. 【请求】Request Method: Get/Post
    print(request.method)

    # 2. 【请求】Get Parameters in Urls
    print(request.GET)  # <QueryDict: {'n1': ['10'], 'n2': ['100']}>

    # 3. 【请求】Get Parameters in Request Body
    print(request.POST)

    # 4. 【响应】HttpResponse("Something"): Return the string
    # return HttpResponse("Something")

    # 5. 【响应】读取HTML内容，然后渲染替换，生成新的字符串给用户的浏览器返还回去
    # return render(request, "something.html")

    # 6. 【响应】redirect to other pages
        # 6.1: 浏览器向网站发送请求，网站告诉浏览器去哪里，浏览器再自己去访问
    return redirect("https://www.baidu.com")
```



## 案例：用户登陆

- CSRF Problem: Forbidden (403) - CSRF verification failed. Request aborted.
  - 添加 {% csrf_token %} 在Form表单中
  - 作用：In Django, the CSRF token is a security measure to prevent Cross-Site Request Forgery (CSRF) attacks by validating a token in form submissions to ensure the legitimacy of requests.

```
views.py

def login(request):
    # if it is a GET request
    if request.method=="GET":
        return render(request, "login.html")
    # if it is a POST request
    print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == "admin" and password == "123456":
        # return HttpResponse("Login Success")
        return redirect("https://www.google.com")
    
    return render(request, "login.html", {"error": "Wrong username or password"})
```

知识点：

- 模版语法
- 请求与响应



## 7. PyMysql数据库操作

**Start MySQL**

```sh
sudo /usr/local/mysql/support-files/mysql.server start
```

**Stop MySQL**

```sh
sudo /usr/local/mysql/support-files/mysql.server stop
```

**Restart MySQL**

```sh
sudo /usr/local/mysql/support-files/mysql.server restart
```

### 7.1 PyMySql-创建数据

```
pip install pymysql
```

```
import pymysql
# 1. Connect Database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='cc20010712', charset='utf8', db="shoes")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 收发指令的工具

# 2. Execute SQL, Object形式
while True:
    username = input("Enter your username: ")
    if username.upper() == "Q":
        break
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    
    sql = "INSERT INTO Users(userName, password, email) VALUES (%(n1)s, %(n2)s, %(n3)s)"
    cursor.execute(sql, {"n1": username, "n2": password, "n3": email})
    conn.commit()

# 3. Close
cursor.close()
conn.close()
```

- Avoid using string concatenation字符串拼接 to construct SQL queries, as it can lead to SQL injection attacks.

```
ARRAY 形式
sql = "INSERT INTO Users(userName, password, email) VALUES (%s, %s, %s)"
cursor.execute(sql, ["yovan_peng", "password999", "yovan@peng.com"])
conn.commit()
```

### 7.1 PyMySql-查询数据

```
import pymysql

# 1. Connect Database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='cc20010712', charset='utf8', db="shoes")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 收发指令的工具

# 2. Execute SQL
cursor.execute("SELECT * FROM Users")
data = cursor.fetchall()  # 获取返回回来的值，[{...}, {...},...,{...}]
print(data)

# 3. Close
cursor.close()
conn.close()
```

```
fetchone()
获取符合条件的第一个数据, {...}
```

## 8. Django ORM 框架

1			2			3					4

代码		ORM		pymysql			数据库

​						MySQLdb

​						mysqlclient

​           model.xxx.all()  -> select * from...

- 之前用pymql都要写sql语句例如 `select * from ...`
- ORM让开发者不用写sql语句，更加简单，例如 `models.xxx.all()`

**ORM的作用：**

- 创建，修改和删除数据库中的表（不用写SQL语句）（无法创建数据库）
- 操作表中的数据例如select，insert

### 8.1 连接数据库

```
settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "DJANGO",
        "USER": "root",
        "PASSWORD": "cc20010712",
        "HOST": "localhost",
        "PORT": "3306",  # typically '3306' for MySQL
    }
}
```

### 8.2 操作表

- 创建
- 删除
- 修改

```
models.py

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

"""
create table app01_UserInfo(
    id bigint auto_increment primary key,       自动生成
    name varchar(32),
    password varchar(64),
    age int,
)
"""
```

`makemigrations`: generates migration files based on the changes made to your models

`migrate`: applies these migration files to the database, updating its schema accordingly.

```
python manage.py makemigrations
python manage.py migrate
```



- 想要删除一列，直接Comment掉

```
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # age = models.IntegerField()
```

- 想要新增一列，例如新增address

```
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # age = models.IntegerField()
    address = models.CharField(max_length=128)
```

会遇到如下问题：

```
It is impossible to add a non-nullable field 'address' to userinfo without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 
```

`选项1`：输入一个默认值，所有之前已经存在的数据，在新增那一列的值都会是这个默认值

`选项2`：自己去文件里添加一个默认值，比如：

```
address = models.CharField(max_length=128, default="adelaide")
```

`选项3`：允许为空

```
address = models.CharField(max_length=128, null=True, blank=True)
```

### 8.3 增删改查

```
views.py

from app01 import models
def orm(request):
    # Test ORM CRUD

    # 1. CREATE
    models.Department.objects.create(title='Sales')
    models.Department.objects.create(title='Marketing')
    models.UserInfo.objects.create(name='Yovan', password='123456', age=23, address='Shanghai')
    models.UserInfo.objects.create(name='Arial', password='456789', age=24, address='Guangzhou')

    # 2. DELETE
    models.Department.objects.filter(id='3').delete()          # filter() 筛选
    models.Department.objects.all().delete()                   # all() 全选

    # 3. READ
    user_list = models.UserInfo.objects.all()
    for user in user_list:
        print(user.id, user.name, user.age, user.address)
    
    user_query_list = models.UserInfo.objects.filter(id="1")  # retuen query list
    user_obj = models.UserInfo.objects.filter(id="1").first() # if only one object, user first

    # 4. UPDATE
    models.UserInfo.objects.all().update(password="999999")
    models.UserInfo.objects.filter(id="1").update(password="889911")

    return HttpResponse("Success")
```



## 案例：用户管理

- 展示用户列表
- 添加用户
- 删除用户

127.0.0.1:8000/info/delete/?nid=3

http://127.0.0.1:8000/list/delete/?nid=4



# Day2 Application

主题：员工管理系统

## 1. Start Project

- Create Skeleton

```
django-admin startproject <PROJECT_NAME>
```

- Create and Sign Up Apps

```
python manage.py startapp <APP_NAME>
```

```
settings.py
"app01.app.App01Config"
```



## 2. Database Schema Design

- CharField 必须有 max_length

1. ID/部门名字？
   - ID：数据库范式，节省存储开销
   - 名字：查询次数多，连表操作耗时，加速查找，允许数据冗余
2. Foreign Key值的约束
   - `-to: to which table`
   -  `-to_field: to which field/column`

3. 如果部门被删除

   - 删除用户，级联删除`on_delete=models.CASCADE`

   - 置空，`on_delete=models.SET_NULL, null=True, blank=True`

```
# Create your models here.
""" Department Table """
class Department(models.Model):
    id = models.BigAutoField(verbose_name="ID", primary_key=True)
    title = models.CharField(verbose_name= "标题",max_length=32)

""" Staff Table"""
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    """ 长度为10 小数为2 默认为0 """
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0) 
    create_time = models.DateTimeField(verbose_name="入职时间")

    # MySQL Restriction
    # Non-Restricted Foreign Key
    # depart = models.BigAutoField(verbose_name="部门ID")
    
    # 1. Restricted Foreign Key
    # -to: to which table
    # -to_field: to which field/column
    # 2. digango auto generate an '_id' post_fix for foreign key attributes
    depart = models.ForeignKey(verbose_name="部门ID",to="Department",to_field="id",
                               on_delete=models.SET_NULL, null=True, blank=True)
    
    # Django Restriction
    gender_choices = (
        (1,"男"),
        (2,"女")
        )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)
```



## 3. Create DB & Tables

- Start MySQL Locally and Create the Database

```
mysql -u root -p
CREATE DATABASE <db_name>;
```

- Update Project's settings.py File

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "DJANGO_DAY2",
        "USER": "root",
        "PASSWORD": "cc20010712",
        "HOST": "localhost",  # This should be the hostname, typically 'localhost' for local MySQL server
        "PORT": "3306",  # This should be the port number, typically '3306' for MySQL
    }
}
```

- Create Tables Using Django Commands

```
python manage.py makemigrations
python manage.py migrate
```



## 4. Manage Department

> Try the most primal/original way to do. 
>
> Django provides Form and ModelForm. 

- Department List 
  - Department Create/Delete/Update/Read

```
def depart_list(request):
    # Get all departments
    department_list_db = models.Department.objects.all() # query set: object lists

    return render(request, 'depart_list.html', {'department_list': department_list_db})

def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    
    #     if request.method == 'POST':
    depart_to_add = request.POST.get('DepartmentName') #绑定的input的name attribute
    models.Department.objects.create(title=depart_to_add)
    return redirect('/depart/list/')

def depart_delete(request):
    # /depart/delete/?id=1
    # get the id from the url
    nid = request.GET.get('nid')
    
    # delete
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_edit(request, nid):
    if request.method == 'GET':
        departName_db = models.Department.objects.filter(id=nid).first().title
        return render (request, 'depart_edit.html', {"departName": departName_db})
    
    new_depart_name = request.POST.get('DepartmentName')
    models.Department.objects.filter(id=nid).update(title=new_depart_name)
    return redirect('/depart/list/')
```



## 5. Templates Inheritance

- `{% block content %}{% endblock %}`

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1-dist/css/bootstrap.css' %}" />
</head>
<body>
    <!-- navigation  -->
    <nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"> Yovan Department Management System </a>
          </div>

          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
              <li><a href="#">Department Management</a></li>
              <li><a href="#">[PlaceHolder]</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="#">Link</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Account <span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Profile</a></li>
                  <li role="separator" class="divider"></li>
                  <li><a href="#">Sign Out</a></li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
    </nav>

    <div>
        {% block content %}{% endblock %}
    </div>

    <!-- <footer></footer> -->
    <script src="{% static 'plugins/jquery/jquery-3.7.1.js' %}"></script>
    <script src="{% static 'plugins/bootstrap-3.4.1-dist/js/bootstrap.js' %}"></script>
</body>
</html>
```

```
{% extends 'layout.html' %}
{% block content %}
    <h1>这是首页</h1>
{% endblock %}
```

> Syntax Below

```
Define: 
{% block <BLOCKNAME> %}
{% endblock %}

Usage:
{% extends '<>.html' %}
{% block <BLOCKNAME> %}
	<...>
{% endblock %}
```

比如 block css, block title....

```
INSERT INTO app01_userinfo(name, password, age, account, create_time, gender, depart_id) values("Yovan", "2000", 23, 90100.68, "2023-9-1", 1, 1);

INSERT INTO app01_userinfo(name, password, age, account, create_time, gender, depart_id) values("Arial", "2200", 24, 80100.68, "2025-9-1", 2, 6);

INSERT INTO app01_userinfo(name, password, age, account, create_time, gender, depart_id) values("Ack", "123123", 99, 520, "2029-9-1", 1, 5);

```



## 6. Manage User

- Original Way
  - Input Validation 
  - If Error, 页面提示
- Form(Easier) and ModelForm(Easiest)



## 7. Form&ModelForm

#### 0. app - Models.py

- We have database schema in the Models.py 

```python
""" Staff Table"""
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0) 
    create_time = models.DateTimeField(verbose_name="入职时间")
    depart = models.ForeignKey(verbose_name="部门ID",to="Department",to_field="id",
                       on_delete=models.SET_NULL, null=True, blank=True)
    gender_choices = (
        (1,"男"),
        (2,"女")
        )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)
```

#### 1. app - views.py

- For `form method`  we define a class using `From`
- create variable form using thatclass

```python
class MyForm(Form):
	user = forms.CharField(widget=forms.Input)
	pwd = forms.CharField(widget=forms.Input)
	email = forms.CharField(widget=forms.Input)
	
def user_add(request):
	if request.method == "GET":
		form = MyForm()
		return render(request, "add.html", {"form": form})
```

#### 2. add.html

- For `form` methods

```python
<form>
	{{form.user}}
	{{form.pwd}}
	{{form.email}}
</form>
```

- For `ModelForm` methods
  - `field` has attributes like label, title

```python
<form method="POST" novalidate>
                {% csrf_token %}
                {% for field in form %}
                <div class="form-group">
                  <label for="{{field.title}}">{{field.label}}</label>
                  {{ field }}
                  <span style="color:red">{{field.errors.0 }}</span>
                  <!-- <input type="text" class="form-control" name="UserName" placeholder="Enter User Name"> -->
                </div>
                {% endfor %}
                <button type="submit" class="btn btn-default">Submit</button>
            </form>
```

#### 3. app - views.py ModelForm (Recomannd)

```python
from django import forms
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}
```

#### 4. views.py - Handle POST Request

- Save to the database
- Send back error messages

```
def user_model_form_add(request):
    # model form version of user add
    if request.method == 'GET':    
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})
    
    # 2. Handle POST Request
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # Save to DB
        form.save()
        return redirect('/user/list/')
    
    return render(request, 'user_model_form_add.html', {"form": form})
```



## Day3

- Department Management

- User Management

  - User List
  - Add User

  ```
  ModelForm: For one table in the database
  Form: 
  ```

  















