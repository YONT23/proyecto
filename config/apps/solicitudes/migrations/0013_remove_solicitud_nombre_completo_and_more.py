# Generated by Django 4.2.4 on 2023-08-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0012_anexos_status_autorxsolicitud_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='nombre_completo',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='nombre_completo2',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='autores',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
