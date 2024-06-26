from django.shortcuts import render, HttpResponse

# Create your views here.

# reques: default parameter
def index(request):
    return HttpResponse("Welcome")

def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return HttpResponse("User Add")