# Generated by Django 4.1.2 on 2022-11-04 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0010_alter_equipe_grupo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grupos',
            new_name='Grupo',
        ),
    ]