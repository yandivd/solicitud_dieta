# Generated by Django 3.2.8 on 2022-08-07 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_solicitud_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterModelOptions(
            name='solicitud',
            options={'verbose_name': 'Solicitud', 'verbose_name_plural': 'Solicitudes'},
        ),
        migrations.AlterModelOptions(
            name='trabajador',
            options={'verbose_name': 'Trabajador', 'verbose_name_plural': 'Trabajadores'},
        ),
        migrations.AlterModelOptions(
            name='unidad_organizativa',
            options={'verbose_name': 'Unidad Organizativa', 'verbose_name_plural': 'Unidades Organizativas'},
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.provincia'),
            preserve_default=False,
        ),
    ]