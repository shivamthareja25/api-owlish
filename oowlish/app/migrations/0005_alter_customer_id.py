# Generated by Django 3.2.4 on 2021-06-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
