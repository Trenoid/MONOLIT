from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Categories, Projects

from main.models import FAQ

def index(request):

    faqs = FAQ.objects.all()

    context = {
        'title' : 'Monolith',
        'faqs' : faqs
    }

    return render(request,'main/index.html',context)


def about(request):
    context = {
        'title' : 'О компании',
    }
        
    return render(request,"main/about-company.html",context)

def services(request):
    context = {
        'title' : 'Услуги',
    }
        
    return render(request, "main/services.html")