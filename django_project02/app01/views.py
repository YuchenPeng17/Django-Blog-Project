from django.shortcuts import render, redirect
from app01 import models
# Create your views here.
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