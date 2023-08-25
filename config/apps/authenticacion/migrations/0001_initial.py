# Generated by Django 4.2.4 on 2023-08-24 01:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
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
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100)),
                ('resetToken', models.CharField(blank=True, max_length=256, null=True)),
                ('avatar', models.ImageField(upload_to='')),
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
            name='Document_types',
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
            name='Genders',
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
            name='Resources',
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
            ],
            options={
                'verbose_name': 'Resources',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='Resources_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('resourcesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='authenticacion.resources')),
            ],
            options={
                'verbose_name': 'Resources_roles',
                'verbose_name_plural': 'Resources_roles',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('resources', models.ManyToManyField(related_name='roles_resources', through='authenticacion.Resources_roles', to='authenticacion.resources')),
            ],
            options={
                'verbose_name': 'Roles',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='User_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('rolesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='authenticacion.roles')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_roles',
                'verbose_name_plural': 'user_roles',
                'unique_together': {('userId', 'rolesId')},
            },
        ),
        migrations.AddField(
            model_name='roles',
            name='users',
            field=models.ManyToManyField(related_name='roles_user', through='authenticacion.User_roles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resources_roles',
            name='rolesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resouces_roles', to='authenticacion.roles'),
        ),
        migrations.AddField(
            model_name='resources',
            name='roles',
            field=models.ManyToManyField(related_name='resources_roles', through='authenticacion.Resources_roles', to='authenticacion.roles'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(related_name='user_roles', through='authenticacion.User_roles', to='authenticacion.roles'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Persons',
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
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_types', to='authenticacion.document_types')),
                ('gender_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gender_types', to='authenticacion.genders')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons',
                'verbose_name_plural': 'Persons',
                'unique_together': {('name', 'identification')},
            },
        ),
    ]