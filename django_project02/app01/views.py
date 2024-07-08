from django.shortcuts import render, redirect
from app01 import models
# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    #     /depart/edit/?nid=1
    if request.method == 'GET':
        departName_db = models.Department.objects.filter(id=nid).first().title
        return render (request, 'depart_edit.html', {"departName": departName_db})
    
    new_depart_name = request.POST.get('DepartmentName')
    models.Department.objects.filter(id=nid).update(title=new_depart_name)
    return redirect('/depart/list/')

def user_list(request):
    user_list_db = models.UserInfo.objects.all()
    for obj in user_list_db:
        obj.create_time = obj.create_time.strftime("%Y-%m-%d")
        # 1. Django Choices
        obj.gender = obj.get_gender_display()
        
        # 2. Django Foreign Key
        # obj.depart_id = models.Department.objects.filter(id=obj.depart_id).first().title
        # !: Django 自动获取连表的内容
        obj.depart_id = obj.depart.title

    return render(request, 'user_list.html', {"user_list": user_list_db})

