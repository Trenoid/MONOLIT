import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from sqlalchemy import ForeignKey
from projects.models import Projects
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.timezone import now

from django.conf import settings


# send_mail(
#     'Тестовое письмо',
#     'Это тестовое сообщение.',
#     settings.EMAIL_HOST_USER,
#     ['gcfhcjh@gmail.com'],
#     fail_silently=False,
# )
# class User(AbstractUser):

#     RECOMMENDATION_STATUS_CHOICES = [
#         ('silver', 'Серебро'),
#         ('gold', 'Золото'),
#         ('platinum', 'Платинум'),
#     ]
#     PROJECT_COMPLETION_PERCENTAGE_CHOICES = [
#         (0,0),
#         (25,25),
#         (50,50),
#         (75,75),
#         (100,100),
#     ]
    

#     recommendation_status = models.CharField(
#         max_length=10,
#         choices=RECOMMENDATION_STATUS_CHOICES,
#         default='silver',
#         verbose_name= "Статус рекомендации"
#     )
#     download_link = models.URLField(blank=True, null=True,verbose_name="Ссылка на скачивание")
#     project_completion_percentage = models.PositiveIntegerField(default=0,
#                                                                 choices= PROJECT_COMPLETION_PERCENTAGE_CHOICES, 
#                                                                 verbose_name="Процент завершенности проекта")
    

#     balance = models.DecimalField(default = 0, max_digits = 9 , decimal_places = 2, verbose_name = "Баланс пользователя")

#     phone = models.CharField(max_length=20, blank=True, null=True, verbose_name= "Номер телефона")
#     city = models.CharField(max_length=100, blank=True, null=True, verbose_name= "город")
#     referal_code = models.CharField(max_length=30,blank=True,null=True,verbose_name="Реферальный код")
#     referal_code_used = models.PositiveIntegerField(default=0, verbose_name= "Число использований реферального кода пользователя")


#     is_verified_email = models.BooleanField(default=False)

#     class Meta:
#         db_table = "user"
#         verbose_name = "Пользователя"
#         verbose_name_plural = "Пользователи"

#     def __str__(self):
#         return self.username
    

# class EmailVerification(models.Model):
#     code = models.UUIDField(unique=True)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     expiration = models.DateTimeField( )

#     def __str__(self) -> str:
#         return f"EmailVerification object for{self.user}"

#     def send_verification_email(self):
#         link=reverse("users:email_ver",kwargs={"email":self.user.email,"code" : {self.code}})
#         verification_link = f"{settings.DOMAIN_NAME}{link}" 
#         subject = f"Подтверждение учетной записи для {self.user.username}"
#         message = f"Для подтверждения учетной записи для {self.user.email} перейдите по ссылке {verification_link}"
        
#         send_mail(
#     subject=subject,
#     message=message,
#     from_email="from@example.com",
#     recipient_list= [self.user.email],
#     fail_silently=False,
#         )

class User(AbstractUser):
    RECOMMENDATION_STATUS_CHOICES = [
        ('silver', 'Серебро'),
        ('gold', 'Золото'),
        ('platinum', 'Платинум'),
    ]
    PROJECT_COMPLETION_PERCENTAGE_CHOICES = [
        (0, 0),
        (25, 25),
        (50, 50),
        (75, 75),
        (100, 100),
    ]

    recommendation_status = models.CharField(
        max_length=10,
        choices=RECOMMENDATION_STATUS_CHOICES,
        default='silver',
        verbose_name="Статус рекомендации"
    )
    download_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на скачивание")
    project_completion_percentage = models.PositiveIntegerField(
        default=0,
        choices=PROJECT_COMPLETION_PERCENTAGE_CHOICES,
        verbose_name="Процент завершенности проекта"
    )
    balance = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Баланс пользователя"
    )
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    referal_code = models.CharField(max_length=30, blank=True, null=True, verbose_name="Реферальный код")
    referal_code_used = models.PositiveIntegerField(default=0, verbose_name="Число использований реферального кода пользователя")
    is_verified_email = models.BooleanField(default=False, verbose_name="Подтвержден ли email")

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f"EmailVerification object for {self.user}"

    def send_verification_email(self):
        link = reverse("users:email_ver", kwargs={"email": self.user.email, "code": self.code})
        verification_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Подтверждение учетной записи для {self.user.username}"
        message = f"Для подтверждения учетной записи для {self.user.email} перейдите по ссылке {verification_link}"
        

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    
class OrderitemQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.projects_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(1 for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа", blank=True, null=True,)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True,)
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено", blank=True, null=True,)
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа", blank=True, null=True,)

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    project = models.ForeignKey(to=Projects, on_delete=models.SET_DEFAULT, null=True, verbose_name="Проект", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")


    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderitemQueryset.as_manager()

    def projects_price(self):
        return round(self.project.sell_full_price() ,2)

    def __str__(self):
        return f"Проект {self.name} | Заказ № {self.order.pk}"
    



