# Generated by Django 2.2.1 on 2019-05-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_cartitems_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='vieworders',
            name='topping',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
