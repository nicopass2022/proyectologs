# Generated by Django 4.0.4 on 2022-04-13 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_remove_articulos_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='descripcion',
        ),
    ]
