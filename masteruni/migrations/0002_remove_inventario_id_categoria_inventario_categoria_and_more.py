# Generated by Django 5.0.6 on 2024-06-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masteruni', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='id_categoria',
        ),
        migrations.AddField(
            model_name='inventario',
            name='categoria',
            field=models.CharField(default='categoria', max_length=30),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
