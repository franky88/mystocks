# Generated by Django 4.0.2 on 2022-03-04 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_stock_total_share'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='total_share',
        ),
    ]
