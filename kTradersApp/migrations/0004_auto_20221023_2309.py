# Generated by Django 3.1.3 on 2022-10-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kTradersApp', '0003_auto_20221022_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerdetails',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ownerdetails',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]