from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def Qsomos(request):
    return render(request,"core/Qsomos.html")
