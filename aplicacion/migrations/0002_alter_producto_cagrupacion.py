# Generated by Django 4.2.3 on 2024-02-10 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cAgrupacion',
            field=models.CharField(choices=[('Cj', 'Cj'), ('Pqte', 'Pqte'), ('Und', 'Und')], default='Unidad', max_length=120, verbose_name='Agrupación'),
        ),
    ]
