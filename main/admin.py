from django.contrib import admin
from django.contrib import admin

from main.models import FAQ, Contact_informations

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)



admin.site.register(Contact_informations)