# Generated by Django 2.2.17 on 2021-01-17 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_curso_duracao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='habilidade',
            name='descricao',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Perfil')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='OportunidadePerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oportunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Oportunidade')),
            ],
        ),
        migrations.CreateModel(
            name='CursoPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Curso')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='CasePerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Case')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Perfil')),
            ],
        ),
    ]
