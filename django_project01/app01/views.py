from django.shortcuts import render, HttpResponse

# Create your views here.

# reques: default parameter
def index(request):
    return HttpResponse("Welcome")