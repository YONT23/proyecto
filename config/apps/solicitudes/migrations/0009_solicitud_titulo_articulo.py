# Generated by Django 4.1.7 on 2023-06-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0008_solicitud_nombre_completo_solicitud_nombre_completo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='titulo_articulo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]