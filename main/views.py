from typing import Any
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import context
from projects.models import Categories, Projects
from django.views.generic.base import TemplateView
from django.http import JsonResponse

from main.forms import ContactForm
from main.models import FAQ



class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faqs = FAQ.objects.all()
        context['title'] = 'Monolith'
        context['faqs'] = faqs
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (например, отправка email)
            # name = form.cleaned_data['name']
            # phone_number = form.cleaned_data['phone_number']
            # city = form.cleaned_data['city']
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})






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
        
    return render(request, "main/services.html",context)

def quiz(request):
    context={
        'title' : "Квиз"
    }

    return render(request,"main/quiz.html",context)