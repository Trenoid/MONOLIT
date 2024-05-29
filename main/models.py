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
