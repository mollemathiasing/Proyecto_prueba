# Generated by Django 4.1.1 on 2022-11-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
