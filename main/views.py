from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title' : 'Home',
        'content' : "Content"
    }

    return render(request,'main/index.html',context)


def about(request):
    return render(request,"main/about-company.html")

def services(request):
    return render(request, "main/services.html")