from atexit import register
from django.contrib import admin

from projects.models import Categories, Projects

#admin.site.register(Categories)
#admin.site.register(Projects)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" :("floor",)}

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" :("name",)}
