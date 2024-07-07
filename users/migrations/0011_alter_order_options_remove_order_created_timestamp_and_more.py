# Generated by Django 4.2.13 on 2024-06-14 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_referralcode_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_timestamp',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='basket_history',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='initiator',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='promocod',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Создан'), (1, 'Оплачен'), (2, 'Закончен')], default=0),
        ),
        migrations.AlterModelTable(
            name='order',
            table=None,
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
