from django.urls import path

from projects.views import catalog, project

app_name = "projects"

urlpatterns = [
    path('', catalog, name='index'),
    path('project/<slug:project_slug>/', project, name='project'),

]
