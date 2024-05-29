from django.contrib import admin
from django.contrib import admin

from main.models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
