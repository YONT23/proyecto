# Generated by Django 4.2.4 on 2023-10-02 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0017_alter_solicitud_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='fecha',
            new_name='fecha_creacion',
        ),
    ]
