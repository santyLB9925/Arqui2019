# Generated by Django 2.2.1 on 2019-07-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0002_asistencia_fechacompare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='fechaCompare',
            field=models.IntegerField(default='20190703'),
        ),
    ]