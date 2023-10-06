# Generated by Django 4.2.4 on 2023-09-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticacion', '0003_person_orcid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document_type',
            new_name='DocumentType',
        ),
        migrations.RenameModel(
            old_name='Resource_rol',
            new_name='ResourceRol',
        ),
        migrations.RenameModel(
            old_name='User_rol',
            new_name='UserRol',
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Document Type', 'verbose_name_plural': 'Document Types'},
        ),
        migrations.RenameField(
            model_name='resourcerol',
            old_name='resourcesId',
            new_name='resource',
        ),
        migrations.RenameField(
            model_name='resourcerol',
            old_name='rolesId',
            new_name='role',
        ),
        migrations.AddField(
            model_name='person',
            name='url_orcid',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]