# Generated by Django 4.2.13 on 2024-06-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_his_referral_code_alter_user_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='his_referral_code',
        ),
        migrations.AddField(
            model_name='user',
            name='referal_code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Реферальный код'),
        ),
    ]
