# Generated by Django 2.2.17 on 2021-01-17 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_oportunidadeperfil_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilidade',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='perfil_empreendedor',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='texto_personalidade',
        ),
    ]
