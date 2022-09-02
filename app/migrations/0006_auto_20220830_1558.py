# Generated by Django 3.2.8 on 2022-08-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220827_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_Contable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='c_contable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.c_contable'),
        ),
    ]