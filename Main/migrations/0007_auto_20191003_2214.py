# Generated by Django 2.2.5 on 2019-10-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20190927_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='header',
            field=models.CharField(max_length=100),
        ),
    ]
