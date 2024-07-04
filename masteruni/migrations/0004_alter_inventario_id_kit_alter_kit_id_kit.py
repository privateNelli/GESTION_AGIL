# Generated by Django 5.0.6 on 2024-07-01 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masteruni', '0003_kit_inventario_id_kit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='id_kit',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='masteruni.kit'),
        ),
        migrations.AlterField(
            model_name='kit',
            name='id_kit',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
