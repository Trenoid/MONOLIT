from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import ReferralCode
import string, random

User = get_user_model()

@receiver(post_save, sender=User)
def create_referral_code(sender, instance, created, **kwargs):
    if created and not instance.referral_code:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        while ReferralCode.objects.filter(code=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        referral_code = ReferralCode.objects.create(code=code)
        instance.referral_code = referral_code
        instance.save()