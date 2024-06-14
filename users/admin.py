from atexit import register
from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User, EmailVerification,ReferralCode

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email","phone", "recommendation_status", "project_completion_percentage", "referral_code"]
    search_fields = ["username", "email","phone", "recommendation_status", "project_completion_percentage", "referral_code"]
    list_filter = ["recommendation_status", "project_completion_percentage"]

    inlines = [CartTabAdmin,]

    def get_referral_code(self, obj):
        return obj.referral_code.code if obj.referral_code else None
    get_referral_code.short_description = 'Referral Code'

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code',"user","expiration")
    fields = ('code',"user","expiration", "created")
    readonly_fields = ("created",)


admin.site.register(ReferralCode)