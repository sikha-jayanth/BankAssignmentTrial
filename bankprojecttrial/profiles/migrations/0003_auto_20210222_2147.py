# Generated by Django 3.1.4 on 2021-02-23 05:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210222_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='transaction_date',
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_date_time',
            field=models.DateField(default=datetime.datetime(2021, 2, 22, 21, 47, 1, 50095), verbose_name='date and time'),
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='date_opened',
            field=models.DateField(default=datetime.datetime(2021, 2, 22, 21, 47, 1, 49097)),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=100)),
                ('account_pin', models.IntegerField()),
                ('transfer_date_time', models.TimeField(default=datetime.datetime(2021, 2, 22, 21, 47, 1, 50095), verbose_name='date and time')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.accountinfo')),
            ],
        ),
    ]
