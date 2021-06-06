# Generated by Django 3.2.4 on 2021-06-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('sale_amount', models.IntegerField(max_length=10)),
                ('lattitude', models.FloatField(blank=True, max_length=20, null=True)),
                ('longitude', models.FloatField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
