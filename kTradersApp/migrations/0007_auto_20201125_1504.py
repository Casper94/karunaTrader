# Generated by Django 3.1.3 on 2020-11-25 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kTradersApp', '0006_auto_20201125_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='driver_contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='txn_date',
            field=models.DateField(default=datetime.date(2020, 11, 25)),
        ),
    ]
