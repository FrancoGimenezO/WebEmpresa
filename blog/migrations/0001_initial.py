# Generated by Django 5.0.2 on 2024-02-29 01:19

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Nombre')),
                ('created', models.TimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.TimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Nombre')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('published', models.DateTimeField(default=datetime.datetime(2024, 2, 29, 1, 19, 55, 352988, tzinfo=datetime.timezone.utc), verbose_name='Hora de publicacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
                ('created', models.TimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.TimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(to='blog.category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-created'],
            },
        ),
    ]
