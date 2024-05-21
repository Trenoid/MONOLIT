from unicodedata import category
from django.db import models

class Categories(models.Model):
    floor  =   models.CharField(max_length=150,unique=True, verbose_name= "Этажность")
    slug = models.SlugField(max_length=200,unique=True,blank=True,null = True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.floor


class Projects(models.Model):
    name = models.CharField(max_length=150,unique=True, verbose_name= "Название")
    slug = models.SlugField(max_length=200,unique=True,blank=True,null = True, verbose_name="URL")
    price_project = models.DecimalField(default=40000.00,max_digits=10,decimal_places=2,verbose_name="Цена проекта")
    image = models.ImageField(upload_to="projects_images",blank=True,null=True,verbose_name="Изображение")
    discount = models.DecimalField(default=40000.00,max_digits=10,decimal_places=2,verbose_name="Скидка в %")
    floor = models.ForeignKey(to = Categories,on_delete=models.PROTECT,verbose_name="Этажность")

    foundation = models.CharField(max_length=10000,verbose_name= "Фундамент")
    wall_material = models.CharField(max_length=10000, verbose_name="Материал стен")
    overlap = models.CharField(max_length=10000, verbose_name="Покрытие стен")
    tupe_of_roof = models.CharField(max_length=10000,verbose_name="Тип кровли")
    roofing_material = models.CharField(max_length=10000,verbose_name="Кровельный материал")
    exterior_decoration = models.CharField(max_length=10000,verbose_name="Наружная отделка")
    dimension = models.CharField(max_length=10000,verbose_name="Габариты")
    the_area = models.CharField(max_length=10000,verbose_name="Площадь")
    the_cost_of_construction = models.DecimalField(default= 0.00, max_digits=20,decimal_places=2,verbose_name="Стоимость строительства")

    price_arhitectural_project = models.DecimalField(default = 16000, max_digits = 7, decimal_places = 2, verbose_name = "Цена Архитектурный проект")
    price_pleliminary_design = models.DecimalField(default = 9000, max_digits = 7, decimal_places = 2, verbose_name = "Цена Эскизный проект")
    price_3d_visualisation = models.DecimalField(default = 0, max_digits = 7 , decimal_places = 2, verbose_name = "Цена 3д визуализация")
    price_3d_model = models.DecimalField(default = 9000, max_digits = 7 , decimal_places = 2, verbose_name = "Цена 3д модель")
    price_the_foundation_monolithic = models.DecimalField(default = 6000, max_digits = 7 , decimal_places = 2, verbose_name = "Цена Фундамент монолитный")
    price_construction_section = models.DecimalField(default = 14000, max_digits = 7 , decimal_places = 2, verbose_name = "Цена Конструктивный раздел")
    price_construction_estimates = models.DecimalField(default = 9000, max_digits = 7 , decimal_places = 2, verbose_name = "Цена Смета на строительство")
    full_price = models.DecimalField(default = 39900, max_digits = 9 , decimal_places = 2, verbose_name = "Итоговая стоимость со скидкой")


    class Meta:
        db_table = "project"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self) -> str:
        return self.name