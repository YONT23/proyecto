# Generated by Django 4.2.4 on 2023-09-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_alter_usuarioxformacion_cert_grado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidosolicitud',
            name='archivo_adjunto',
            field=models.FileField(upload_to='archivos/archivos_contenido_solicitud/'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='correciones',
            field=models.FileField(blank=True, null=True, upload_to='archivos/archivos_seguimiento/'),
        ),
        migrations.AlterField(
            model_name='usuarioxformacion',
            name='cert_grado',
            field=models.FileField(blank=True, null=True, upload_to='archivos/archivos_user_formacion/'),
        ),
        migrations.AlterField(
            model_name='usuarioxformacion',
            name='cert_resol',
            field=models.FileField(blank=True, null=True, upload_to='archivos/archivos_user_formacion/'),
        ),
        migrations.AlterField(
            model_name='usuarioxformacion',
            name='resol_conv',
            field=models.FileField(blank=True, null=True, upload_to='archivos/archivos_user_formacion/'),
        ),
    ]
