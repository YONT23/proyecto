# Generated by Django 4.2.4 on 2023-09-24 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0009_remove_solicitud_autores_solicitud_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='autor',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='autores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]