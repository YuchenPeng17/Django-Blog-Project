from django.shortcuts import render, HttpResponse

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
    name = "Yuchen"
    comment = "All Good"
    role = ["programmer", "developer", "data analyst"]
    return render(request, "tpl.html", {
        "name": name,
        "comment": comment,
        "role": role,
    })