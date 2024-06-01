from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    RECOMMENDATION_STATUS_CHOICES = [
        ('silver', 'Серебро'),
        ('gold', 'Золото'),
        ('platinum', 'Платинум'),
    ]

    recommendation_status = models.CharField(
        max_length=10,
        choices=RECOMMENDATION_STATUS_CHOICES,
        default='silver'
    )
    download_link = models.URLField(blank=True, null=True)
    project_completion_percentage = models.PositiveIntegerField(default=0)
    his_referral_code = models.CharField(max_length=10, blank=True, null=True)
    referral_code_that_gives_him_a_discount = ...


    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username