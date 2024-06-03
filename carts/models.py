from django.db import models

from projects.models import Projects
from users.models import User



class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        return self.format_number(sum(cart.projects_price() for cart in self))
    
    def total_quantity(self):
        if self:
            return sum(1 for cart in self)
        return 0
    
    def format_number(self, value):
        # Форматируем число с пробелами каждые три цифры
        return '{:,.0f}'.format(value).replace(',', ' ')


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=True,null=True, verbose_name="Пользователь")
    project = models.ForeignKey(to=Projects,on_delete=models.CASCADE, verbose_name="Проект")
    session_key = models.CharField(max_length=32,blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQuerySet().as_manager()
    
    def __str__(self) -> str:
        return f"Корзина {self.user.username} | Проект {self.project.name} | "
    
    
    def projects_price(self):
        return round(self.project.sell_full_price() ,2)
