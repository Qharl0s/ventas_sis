# Generated by Django 4.2.3 on 2024-02-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_producto_cagrupacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmostrador',
            name='cCantidad',
            field=models.CharField(default='', max_length=120, verbose_name='cCantidad'),
        ),
    ]
