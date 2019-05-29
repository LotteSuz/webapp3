# Generated by Django 2.2.1 on 2019-05-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_remove_vieworders_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='vieworders',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
