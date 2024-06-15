from django.shortcuts import render
def index(request):
    context={}
    return render(request,"index.html",context)

from django.shortcuts import render
def login(request):
    context={}
    return render(request,"login.html",context)

from django.shortcuts import render
def registerpg(request):
    context={}
    return render(request,"registerpg.html",context)

from django.shortcuts import render
def welcomepg(request):
    context={}
    return render(request,"welcomepg.html",context)

