# Generated by Django 4.2.4 on 2023-09-28 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0012_remove_usuarioxformacion_cert_resol_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='orcid',
        ),
    ]