# Generated by Django 3.2.8 on 2022-08-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220827_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='observaciones',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='observaciones',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]