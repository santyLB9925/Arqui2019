# Generated by Django 2.2.1 on 2019-07-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='fechaCompare',
            field=models.IntegerField(default=1),
        ),
    ]
