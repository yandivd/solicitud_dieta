# Generated by Django 3.2.8 on 2022-08-11 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_modelo_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelo',
            old_name='nombre',
            new_name='creador',
        ),
    ]
