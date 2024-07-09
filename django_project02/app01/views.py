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

def user_add(request):
    # 1. Handle GET Request
    if request.method == 'GET':
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "depart_list_db": models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    
    # 2. Handle POST Request

    # 2.1 Get the input from user input
    user_in = request.POST.get('UserName')
    pwd_in = request.POST.get('Password')
    age_in = request.POST.get('Age')
    accbalance_in = request.POST.get('AccBalance')
    cretime_in = request.POST.get('CreTime')
    gender_in = request.POST.get('Gender')
    depart_in = request.POST.get('Department')
    
    # 2.2 Add To DB
    models.UserInfo.objects.create(
        name=user_in,
        password=pwd_in,
        age=age_in,
        account=accbalance_in,
        create_time=cretime_in,
        gender=gender_in,
        depart_id=depart_in
    )
    return redirect('/user/list/')


###
from django import forms
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.TextInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}  

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









