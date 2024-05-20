from django.shortcuts import render


def catalog(request):
    context = {
        'title' : 'Каталог проектов',
    }
        
    return render(request,"projects/catalog.html",context)

def project(request):
    context = {
        'title' : 'Проект',
    }
        
    return render(request,"projects/project.html",context)