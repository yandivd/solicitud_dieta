# Generated by Django 3.2.8 on 2022-09-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_solicitud_prov_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='destino',
            field=models.CharField(max_length=50),
        ),
    ]
