# Generated by Django 4.2.4 on 2023-08-21 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0014_rename_responsable_seguimiento_editor_responsable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='editor_responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor_responsable', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='evaluador_responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluador_responsable', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='evaluador_responsable_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluador_responsable_2', to=settings.AUTH_USER_MODEL),
        ),
    ]