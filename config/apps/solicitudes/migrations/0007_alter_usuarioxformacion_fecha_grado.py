# Generated by Django 4.2.4 on 2023-09-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_alter_usuarioxformacion_fecha_grado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioxformacion',
            name='fecha_grado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
