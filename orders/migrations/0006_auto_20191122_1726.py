# Generated by Django 2.0.3 on 2019-11-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_number_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_number',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
