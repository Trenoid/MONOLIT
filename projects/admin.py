from atexit import register
from django.contrib import admin

from projects.models import Categories, Projects

#admin.site.register(Categories)
#admin.site.register(Projects)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" :("floor",)}
    list_display = ["floor", "the_area_filter", "price_filter" ]

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" :("name",)}
    list_display = ["name", "price_project", "discount",]
    list_editable = ["discount",]
    search_fields = ["name",]
    list_filter = ["discount","floor"]
