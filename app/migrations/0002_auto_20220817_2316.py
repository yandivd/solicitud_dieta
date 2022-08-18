# Generated by Django 3.2.8 on 2022-08-17 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo_al_Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=20)),
            ],
        ),
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
        migrations.RemoveField(
            model_name='trabajador',
            name='nombre',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_destino', to='app.municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='numero',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='observaciones',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='origen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_origen', to='app.municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='regreso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_regreso', to='app.municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajador',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.CharField(max_length=100)),
                ('unidad_organizativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unidad_organizativa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PARLEG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('solicitante', models.CharField(max_length=50)),
                ('unidad_organizativa', models.CharField(max_length=100)),
                ('c_contable', models.CharField(max_length=4)),
                ('consec', models.IntegerField()),
                ('parleg', models.CharField(max_length=20)),
                ('autoriza', models.CharField(max_length=50)),
                ('cargo_presupuesto', models.CharField(max_length=20)),
                ('observaciones', models.CharField(max_length=500)),
                ('estado', models.CharField(max_length=10)),
                ('solicitudes', models.ManyToManyField(to='app.Solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='Crea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_organizativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unidad_organizativa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Autoriza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='autoriza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.autoriza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='cargo_presupuesto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cargo_al_presupuesto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='parleg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.parleg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.provincia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.solicitante'),
        ),
    ]
