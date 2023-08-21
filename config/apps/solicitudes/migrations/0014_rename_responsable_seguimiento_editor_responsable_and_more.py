# Generated by Django 4.2.4 on 2023-08-21 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0013_remove_solicitud_nombre_completo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguimiento',
            old_name='responsable',
            new_name='editor_responsable',
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='evaluador_responsable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='editor_responsable_seguimientos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='evaluador_responsable_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='editor_responsable_seguimientos_2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='resultados_evaluacion',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='resultados_evaluacion_2',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]