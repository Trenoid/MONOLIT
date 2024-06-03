from django.contrib import admin

from carts.models import Cart

# Register your models here.

# admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "project","created_timestamp"
    search_fields = "user__username", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display","project","created_timestamp"]
    list_filter = ["created_timestamp","user","project__name",]
    search_fields = ["user__username"]

    def user_display(self,obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    

