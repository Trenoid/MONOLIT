from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Categories, Projects
from django.views.generic.base import TemplateView

from main.models import FAQ



class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        faqs = FAQ.objects.all()
        context =  super(IndexView,self).get_context_data()
        context['title'] = 'Monolith'
        context['faqs'] = faqs
        return context




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