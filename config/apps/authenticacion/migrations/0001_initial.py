# Generated by Django 4.2.4 on 2023-09-14 02:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100)),
                ('resetToken', models.CharField(blank=True, max_length=256, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='archivos/archivos_useravatar/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Document_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Document_types',
                'verbose_name_plural': 'Document_types',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Genders',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('path', models.CharField(max_length=256)),
                ('id_padre', models.IntegerField()),
                ('method', models.CharField(max_length=256)),
                ('icono', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Resources',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='Resource_rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('resourcesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='authenticacion.resource')),
            ],
            options={
                'verbose_name': 'Resources_rols',
                'verbose_name_plural': 'resources_rols',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('resources', models.ManyToManyField(related_name='roles_resource', through='authenticacion.Resource_rol', to='authenticacion.resource')),
            ],
            options={
                'verbose_name': 'Rols',
                'verbose_name_plural': 'rols',
            },
        ),
        migrations.CreateModel(
            name='User_rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('rolesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rols', to='authenticacion.rol')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_rols',
                'verbose_name_plural': 'user_rols',
                'unique_together': {('userId', 'rolesId')},
            },
        ),
        migrations.AddField(
            model_name='rol',
            name='users',
            field=models.ManyToManyField(related_name='roles_rol', through='authenticacion.User_rol', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resource_rol',
            name='rolesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources_rols', to='authenticacion.rol'),
        ),
        migrations.AddField(
            model_name='resource',
            name='roles',
            field=models.ManyToManyField(related_name='resources_rol', through='authenticacion.Resource_rol', to='authenticacion.rol'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(related_name='users_customuser', through='authenticacion.User_rol', to='authenticacion.rol'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('surname', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('identification', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.BooleanField(default=True)),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_types', to='authenticacion.document_type')),
                ('gender_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gender_types', to='authenticacion.gender')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons',
                'verbose_name_plural': 'Persons',
                'unique_together': {('name', 'identification')},
            },
        ),
    ]
