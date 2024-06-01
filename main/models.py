from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True, verbose_name = "Вопрос")
    answer = models.TextField(verbose_name="Овет")

    def __str__(self):
        return self.question
    
    class Meta:
        db_table = "questions"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Contact_informations(models.Model):
    instagramm = models.CharField(max_length=512,verbose_name="Инстаграмм")
    vk = models.CharField(max_length=512,verbose_name="Вконтакте")
    number = models.CharField(max_length=32, verbose_name = "Номер телефона")
    mail_address = models.CharField(max_length=64, verbose_name="Почта")
    telegramm = models.CharField(max_length=64, verbose_name="Почта")

    mail_for_from = models.CharField(max_length=64, verbose_name="Почта для писем из формы")
    
    
    def get_number(self):
        return self.number