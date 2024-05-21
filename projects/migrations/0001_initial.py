# Generated by Django 4.2.13 on 2024-05-21 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=230, unique=True, verbose_name='Этажность')),
                ('slug', models.SlugField(blank=True, max_length=230, null=True, unique=True, verbose_name='URL')),
                ('the_area_filter', models.PositiveIntegerField(default=0, verbose_name='Начниается от скольки метров в квадрате')),
                ('price_filter', models.DecimalField(decimal_places=0, default=0, max_digits=15, verbose_name='Начиная от какой суммы')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('price_project', models.DecimalField(decimal_places=2, default=40000.0, max_digits=10, verbose_name='Цена проекта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects_images', verbose_name='Изображение')),
                ('discount', models.DecimalField(decimal_places=2, default=40000.0, max_digits=10, verbose_name='Скидка в %')),
                ('foundation', models.CharField(max_length=10000, verbose_name='Фундамент')),
                ('wall_material', models.CharField(max_length=10000, verbose_name='Материал стен')),
                ('overlap', models.CharField(max_length=10000, verbose_name='Перекрытие')),
                ('tupe_of_roof', models.CharField(max_length=10000, verbose_name='Тип кровли')),
                ('roofing_material', models.CharField(max_length=10000, verbose_name='Кровельный материал')),
                ('exterior_decoration', models.CharField(max_length=10000, verbose_name='Наружная отделка')),
                ('dimension', models.CharField(max_length=10000, verbose_name='Габариты')),
                ('the_area', models.PositiveIntegerField(default=0, verbose_name='Площадь')),
                ('the_cost_of_construction', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Стоимость строительства')),
                ('price_arhitectural_project', models.DecimalField(decimal_places=2, default=16000, max_digits=7, verbose_name='Цена Архитектурный проект')),
                ('price_pleliminary_design', models.DecimalField(decimal_places=2, default=9000, max_digits=7, verbose_name='Цена Эскизный проект')),
                ('price_3d_visualisation', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена 3д визуализация')),
                ('price_3d_model', models.DecimalField(decimal_places=2, default=9000, max_digits=7, verbose_name='Цена 3д модель')),
                ('price_the_foundation_monolithic', models.DecimalField(decimal_places=2, default=6000, max_digits=7, verbose_name='Цена Фундамент монолитный')),
                ('price_construction_section', models.DecimalField(decimal_places=2, default=14000, max_digits=7, verbose_name='Цена Конструктивный раздел')),
                ('price_construction_estimates', models.DecimalField(decimal_places=2, default=9000, max_digits=7, verbose_name='Цена Смета на строительство')),
                ('full_price', models.DecimalField(decimal_places=2, default=39900, max_digits=9, verbose_name='Итоговая стоимость со скидкой')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.categories', verbose_name='Этажность')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'db_table': 'project',
            },
        ),
    ]