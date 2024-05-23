from django.shortcuts import render
from projects.models import Categories, Projects

def catalog(request):
    catalog = Projects.objects.all()
    context = {
        "title": "Каталог проектов",
        "catalog": catalog,

    }

    return render(request, "projects/catalog.html", context)


def project(request,project_slug):

    project = Projects.objects.get(slug = project_slug)
    context = {
        "title": "Проект",
        "project" : project
    }

    return render(request, "projects/project.html", context)
