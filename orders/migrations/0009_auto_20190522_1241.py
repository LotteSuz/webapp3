# Generated by Django 2.2.1 on 2019-05-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190522_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notpizza',
            name='extracheese',
        ),
        migrations.AlterField(
            model_name='notpizzatoppings',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]