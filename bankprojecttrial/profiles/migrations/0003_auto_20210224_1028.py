# Generated by Django 3.1.6 on 2021-02-24 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210224_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='account_pin',
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='date_opened',
            field=models.DateField(default=datetime.datetime(2021, 2, 24, 10, 28, 30, 149034)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 10, 28, 30, 150033), verbose_name='date and time'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 10, 28, 30, 151033), verbose_name='date and time'),
        ),
    ]
