# Generated by Django 2.2.1 on 2019-05-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_vieworders_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='notpizza',
            name='extratoppings',
            field=models.BooleanField(default=False),
        ),
    ]
