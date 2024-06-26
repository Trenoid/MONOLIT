from unicodedata import category
from django.db import models
from django.urls import reverse
from traitlets import default

class Categories(models.Model):
    floor  =   models.CharField(max_length= 230,unique=True, verbose_name= "Этажность")
    slug = models.SlugField(max_length=230,unique=True,blank=True,null = True, verbose_name="URL")
    the_area_filter = models.PositiveIntegerField(default = 0,verbose_name="Начниается от скольки метров в квадрате")
    price_filter = models.DecimalField(default=0,max_digits = 15,decimal_places=0, verbose_name="Начиная от какой суммы")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


    def __str__(self) -> str:
        return f"{self.floor}"

    def format_number(self, value):
        # Форматируем число с пробелами каждые три цифры
        return '{:,.0f}'.format(value).replace(',', ' ')
    
    def sell_price(self):
        return self.format_number(self.price_filter)
    
    def sell_projects(self):
        return Projects.objects.filter(floor = self.floor).filter(the_area__gt = self.the_area_filter).filter(the_cost_of_construction__gt =self.price_filter )


class Projects(models.Model):
    name = models.CharField(max_length=150,unique=True, verbose_name= "Название")
    slug = models.SlugField(max_length=200,unique=True,blank=True,null = True, verbose_name="URL")
    price_project = models.DecimalField(default=39900,max_digits=10,decimal_places=0,verbose_name="Цена проекта")
    image = models.ImageField(upload_to="projects_images",blank=True,null=True,verbose_name="Изображение")
    discount = models.DecimalField(default=0,max_digits=10,decimal_places=2,verbose_name="Скидка в %")
    floor = models.ForeignKey(to = Categories,on_delete=models.PROTECT,verbose_name="Этажность")

    foundation = models.CharField(max_length=10000,verbose_name= "Фундамент")
    wall_material = models.CharField(max_length=10000, verbose_name="Материал стен")
    overlap = models.CharField(max_length=10000, verbose_name="Перекрытие")
    tupe_of_roof = models.CharField(max_length=10000,verbose_name="Тип кровли")
    roofing_material = models.CharField(max_length=10000,verbose_name="Кровельный материал")
    exterior_decoration = models.CharField(max_length=10000,verbose_name="Наружная отделка")
    dimension = models.CharField(max_length=10000,verbose_name="Габариты")
    the_area = models.PositiveIntegerField(default = 0, verbose_name="Площадь")
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
        ordering = ("id",)


    def __str__(self) -> str:
        return self.name
    
    def format_number(self, value):
        # Форматируем число с пробелами каждые три цифры
        return '{:,.0f}'.format(value).replace(',', ' ')
    
    def sell_price_project(self):
        if self.discount:
            discounted_price = round(self.price_project - self.price_project * self.discount / 100, 2 )
        else:
            discounted_price = self.price_project
        
        return self.format_number(discounted_price)
    
    def no_format_sell_price_project(self):
        if self.discount:
            discounted_price = round(self.price_project - self.price_project * self.discount / 100, 2 )
        else:
            discounted_price = self.price_project
        
        return self.discounted_price

    #def sell_price_project(self):
    #    if self.discount:
    #        return round(self.price_project - self.price_project*self.discount/100,2)
    #    
    #    return self.price_project
    

    def sell_full_price(self):
        if self.discount:
            return round(self.full_price - self.full_price*self.discount/100,2)
        
        return self.full_price
    

    def sell_price_of_construction(self):
        return self.format_number(self.the_cost_of_construction)
    


    def sell_price_arhitectural_project(self):
        return self.format_number(self.price_arhitectural_project)
    

    def sell_price_pleliminary_design(self):
        return self.format_number(self.price_pleliminary_design)
    

    def sell_price_3d_visualisation(self):
        return self.format_number(self.price_3d_visualisation)
    

    def sell_price_3d_model(self):
        return self.format_number(self.price_3d_model)
    

    def sell_price_the_foundation_monolithic(self):
        return self.format_number(self.price_the_foundation_monolithic)
    
    
    def sell_price_construction_section(self):
        return self.format_number(self.price_construction_section)
    
    
    def sell_price_construction_estimates(self):
        return self.format_number(self.price_construction_estimates)
    

    def get_absolute_url(self):
        return reverse("catalog:project", kwargs={"project_slug": self.slug})
    