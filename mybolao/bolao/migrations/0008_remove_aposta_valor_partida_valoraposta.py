# Generated by Django 4.1.2 on 2022-11-01 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0007_remove_equipe_placaraposta1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aposta',
            name='valor',
        ),
        migrations.AddField(
            model_name='partida',
            name='valorAposta',
            field=models.FloatField(null=True),
        ),
    ]