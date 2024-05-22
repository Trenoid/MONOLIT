from django.shortcuts import render
from projects.models import Categories, Projects

def catalog(request):
    categories = Categories.objects.all()
    catalog = Projects.objects.all()
    context = {
        "title": "Каталог проектов",
        "categories" : categories,
        "catalog": catalog,

    }

    return render(request, "projects/catalog.html", context)


def project(request):
    context = {
        "title": "Проект",
    }

    return render(request, "projects/project.html", context)
