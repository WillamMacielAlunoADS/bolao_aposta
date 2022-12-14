# Generated by Django 4.1.2 on 2022-10-31 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placar1', models.IntegerField()),
                ('placar2', models.IntegerField()),
                ('data_criada', models.DateTimeField(default=None, verbose_name='Data Criada')),
                ('data_partida', models.DateTimeField(default=None, verbose_name='Data Partida')),
                ('concluido', models.BooleanField(default=False)),
                ('encerrado', models.BooleanField(default=False)),
                ('equipe1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipe1', to='bolao.equipe')),
                ('equipe2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipe2', to='bolao.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Apostador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, null=True, unique=True)),
                ('telefone', models.CharField(max_length=20, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
