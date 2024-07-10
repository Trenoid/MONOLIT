# Generated by Django 4.2.13 on 2024-06-05 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]