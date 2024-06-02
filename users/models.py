from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    RECOMMENDATION_STATUS_CHOICES = [
        ('silver', 'Серебро'),
        ('gold', 'Золото'),
        ('platinum', 'Платинум'),
    ]
    PROJECT_COMPLETION_PERCENTAGE_CHOICES = [
        (0,0),
        (25,25),
        (50,50),
        (75,75),
        (100,100),
    ]
    

    recommendation_status = models.CharField(
        max_length=10,
        choices=RECOMMENDATION_STATUS_CHOICES,
        default='silver',
        verbose_name= "Статус рекомендации"
    )
    download_link = models.URLField(blank=True, null=True,verbose_name="Ссылка на скачивание")
    project_completion_percentage = models.PositiveIntegerField(default=0,
                                                                choices= PROJECT_COMPLETION_PERCENTAGE_CHOICES, 
                                                                verbose_name="Процент завершенности проекта")
    

    balance = models.DecimalField(default = 0, max_digits = 9 , decimal_places = 2, verbose_name = "Баланс пользователя")

    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name= "Номер телефона")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name= "город")
    referal_code = models.CharField(max_length=30,blank=True,null=True,verbose_name="Реферальный код")
    referal_code_used = models.PositiveIntegerField(default=0, verbose_name= "Число использований реферального кода пользователя")

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username