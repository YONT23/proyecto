# Generated by Django 4.2.4 on 2023-10-05 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0018_rename_fecha_solicitud_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioxformacion',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='usuarioxformacion',
            name='nivel_formacion',
        ),
        migrations.DeleteModel(
            name='NivelFormacion',
        ),
        migrations.DeleteModel(
            name='UsuarioXFormacion',
        ),
    ]
