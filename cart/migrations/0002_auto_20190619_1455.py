# Generated by Django 2.2.1 on 2019-06-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
