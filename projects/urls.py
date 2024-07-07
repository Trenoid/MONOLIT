from django.urls import path

from projects.views import catalog, project
from projects.views import CatalogView
from django.views.decorators.cache import cache_page    

app_name = "projects"

#def views
# urlpatterns = [
#     path('', catalog, name='index'),
#     path('project/<slug:project_slug>/', project, name='project'),
# ]

#class views
urlpatterns = [
    path('',(CatalogView.as_view()) , name='index'),
    path('project/<slug:project_slug>/', project, name='project'),
]

