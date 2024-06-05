from math import floor
from nis import cat
from typing import Any
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from projects.models import Categories, Projects



class CatalogView(TemplateView):
    template_name = "projects/catalog.html"

    def get(self, request):
        on_sale = request.GET.get('on_sale', None)
        order_by = request.GET.get("order_by", None)

        catalog = Projects.objects.all()

        if on_sale:
            catalog = catalog.filter(discount__gt=0)

        if order_by and order_by != "default":
            catalog = catalog.order_by(order_by)

        categories = []
        for category in Categories.objects.all():
            category_projects = catalog.filter(floor=category)
            categories.append(
                {
                    'category': category,
                    'projects': category_projects,
                }
            )

        context = {
            "title": "Каталог проектов",
            "catalog": catalog,
            "categories": categories,
        }
        
        print(f"Final catalog: {list(catalog)}")
        print(f"categories: {categories}")

        return render(request, self.template_name, context)






def catalog(request):

    on_sale = request.GET.get('on_sale',None)
    order_by = request.GET.get("order_by",None)

    catalog = Projects.objects.all()

    if on_sale:
        catalog = catalog.filter(discount__gt=0)

    if order_by and order_by != "default":
        catalog = catalog.order_by(order_by)

 
    categories = []
    for category in Categories.objects.all():
        category_projects = catalog.filter(floor=category)
        categories.append(
            {
                'category': category,
                'projects' : category_projects,
            }
        )
    

    context = {
        "title": "Каталог проектов",
        "catalog": catalog,
        "categories": categories,

    }
    print(f"Final catalog: {list(catalog)}")
    print(f"categories: {categories}")

    return render(request, "projects/catalog.html", context)


def project(request,project_slug):

    project = Projects.objects.get(slug = project_slug)
    context = {
        "title": "Проект",
        "project" : project
    }

    return render(request, "projects/project.html", context)
