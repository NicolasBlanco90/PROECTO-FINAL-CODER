# Generated by Django 4.0.3 on 2022-04-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_blog_fecha_creacion_blog_alter_blog_blog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagen_blog',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
