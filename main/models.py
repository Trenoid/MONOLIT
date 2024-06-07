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
    instagramm = models.CharField(max_length=512,verbose_name="Инстаграмм",default="None")
    vk = models.CharField(max_length=512,verbose_name="Вконтакте",default="None")
    number = models.CharField(max_length=32, verbose_name = "Номер телефона",default="88")
    mail_address = models.CharField(max_length=64, verbose_name="Почта",default="None")
    telegramm = models.CharField(max_length=64, verbose_name="Телеграмм",default="None")

    mail_for_from = models.CharField(max_length=64, verbose_name="Почта для писем из формы",default="None")
    
    

    def get_number(self):
        return self.number
    

    class Meta:
        db_table = "contact_info"
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"