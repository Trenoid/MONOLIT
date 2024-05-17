from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title' : 'Monolith',
        'content' : "Content"
    }

    return render(request,'main/index.html',context)


def about(request):
    context = {
        'title' : 'О компании',
        'content' : "Content"
    }
        
    return render(request,"main/about-company.html",context)

def services(request):
    context = {
        'title' : 'Услуги',
        'content' : "Content"
    }
        
    return render(request, "main/services.html")