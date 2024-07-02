from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.

# reques: default parameter
def index(request):
    return HttpResponse("Welcome")

def user_list(request):
    # 静态文件
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse("User Add")

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
        {
        "name": "Yovan",
        "salary": 70000,
        "role": "graduate job",
        },
        {
        "name": "Osa",
        "salary": 170000,
        "role": "junior job",
        },
        {
        "name": "Levi",
        "salary": 270000,
        "role": "senior job",
        }
    ]
    return render(request, "tpl.html", {
        "name": name_db,
        "comment": comment_db,
        "role": role_db,
        "user_info": user_info_db,
        "data_list": data_list_db,
    })

def something(request):
    # 1. Request Method: Get/Post
    print(request.method)

    # 2. Get Parameters in Urls
    print(request.GET)  # <QueryDict: {'n1': ['10'], 'n2': ['100']}>

    # 3. Get Parameters in Request Body
    print(request.POST)

    # 4. 【响应】HttpResponse("Something"): Return the string
    # return HttpResponse("Something")

    # 5. 【响应】读取HTML内容，然后渲染替换，生成新的字符串给用户的浏览器返还回去
    # return render(request, "something.html")

    # 6. 【响应】redirect to other pages
        # 6.1: 浏览器向网站发送请求，网站告诉浏览器去哪里，浏览器再自己去访问
    return redirect("https://www.baidu.com")

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

def info_list(request):
    # 1. Get All Users Info from Database
    data_list = models.UserInfo.objects.all()


    return render(request, "info_list.html", {
        "data_list": data_list,}
        )

def info_add(request):
    # 1. If receive a GET request
    if request.method == "GET":
        return render(request, "info_add.html")
    # 2. Receuve a POST request
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    address = request.POST.get("address")
    models.UserInfo.objects.create(name=username, password=password, age=age, address=address)
    return redirect("/info/list")

def info_delete(request):
    # 1. Get the id of the user to delete
    nid = request.GET.get("nid")
    # 2. Delete the user
    models.UserInfo.objects.filter(id=nid).delete()
    # 3. Redirect to user list page
    return redirect("/info/list")
