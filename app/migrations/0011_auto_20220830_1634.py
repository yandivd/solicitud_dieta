# Generated by Django 3.2.8 on 2022-08-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_modelo_parleg'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='labor',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='labor',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
