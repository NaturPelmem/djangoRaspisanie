# Generated by Django 4.0.4 on 2022-05-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspisanie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='reduction',
            field=models.BooleanField(default=False, verbose_name='Сокращенка'),
        ),
    ]
