# Generated by Django 5.0.6 on 2024-10-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'ordering': ['-created'], 'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='matricula',
            field=models.CharField(max_length=12, verbose_name='codigo'),
        ),
    ]
