# Generated by Django 4.1.7 on 2023-05-29 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0002_remove_anexos_createdat_remove_anexos_updateat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_asignacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioXFormacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('fecha_grado', models.CharField(max_length=256)),
                ('resol_conv', models.CharField(max_length=256)),
                ('cert_grado', models.CharField(max_length=256)),
                ('nombre_institucion', models.CharField(max_length=256)),
                ('cert_resol', models.CharField(max_length=256)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nivel_formacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.nivelformacion')),
            ],
        ),
        migrations.RemoveField(
            model_name='autorxformacion',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='autorxformacion',
            name='nivel_formacion',
        ),
        migrations.RemoveField(
            model_name='autorxsolicitud',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='autorxsolicitud',
            name='rol_autor',
        ),
        migrations.RemoveField(
            model_name='autorxsolicitud',
            name='solicitud',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='contenidoSolicitud',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.contenidosolicitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='AutorXFormacion',
        ),
        migrations.DeleteModel(
            name='AutorXSolicitud',
        ),
        migrations.DeleteModel(
            name='RolAutor',
        ),
        migrations.AddField(
            model_name='asignaciones',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solicitud'),
        ),
    ]