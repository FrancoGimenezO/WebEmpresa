# Generated by Django 5.0.2 on 2024-02-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.TextField(max_length=200, verbose_name='Subtitulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='servicesw', verbose_name='Imagen')),
                ('created', models.TimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.TimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
