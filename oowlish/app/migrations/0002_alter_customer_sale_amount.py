# Generated by Django 3.2.4 on 2021-06-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sale_amount',
            field=models.IntegerField(),
        ),
    ]