# Generated by Django 4.0.2 on 2022-03-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_alter_buystock_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buystock',
            name='fees',
            field=models.FloatField(blank=True, null=True),
        ),
    ]