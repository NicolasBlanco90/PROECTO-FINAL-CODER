# Generated by Django 4.0.3 on 2022-03-13 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='estudiantes',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('escuela', models.CharField(max_length=50)),
            ],
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='freelancers',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('especialidad', models.CharField(max_length=50)),
            ],
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='profesionales',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('profesion', models.CharField(max_length=50)),
            ],
            bases=('usuarios.usuario',),
        ),
    ]
