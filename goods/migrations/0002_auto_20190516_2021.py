# Generated by Django 2.2.1 on 2019-05-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gcontent',
            field=models.CharField(max_length=2000),
        ),
    ]
