# Generated by Django 4.0.2 on 2022-03-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_remove_stock_total_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='buystock',
            name='total_average_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]