# Generated by Django 3.1.3 on 2020-11-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kTradersApp', '0004_buyer_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_date', models.DateField()),
                ('bill_number', models.IntegerField(unique=True)),
                ('total_amount', models.IntegerField()),
                ('transport_vehicle', models.CharField(max_length=15)),
                ('driver_contact', models.IntegerField()),
                ('vehicle_fare', models.IntegerField()),
                ('pan_num', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kTradersApp.buyer')),
            ],
        ),
    ]
