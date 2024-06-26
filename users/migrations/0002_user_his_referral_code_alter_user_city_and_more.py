# Generated by Django 4.2.13 on 2024-06-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='his_referral_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='recommendation_status',
            field=models.CharField(choices=[('silver', 'Серебро'), ('gold', 'Золото'), ('platinum', 'Платинум')], default='silver', max_length=10, verbose_name='Статус рекомендации'),
        ),
    ]
