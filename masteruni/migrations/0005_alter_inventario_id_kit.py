# Generated by Django 5.0.6 on 2024-07-03 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masteruni', '0004_alter_inventario_id_kit_alter_kit_id_kit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='id_kit',
            field=models.IntegerField(),
        ),
    ]
