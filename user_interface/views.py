from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return HttpResponseRedirect('/login')


def login(request):
    print(request.POST)
    return render(request, "login.html")


def register(request):
    print(request.POST)
    return render(request, "register.html")
