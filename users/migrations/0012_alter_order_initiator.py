# Generated by Django 4.2.13 on 2024-06-14 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_order_options_remove_order_created_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='initiator',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
