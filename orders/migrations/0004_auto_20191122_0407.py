# Generated by Django 2.0.3 on 2019-11-22 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191118_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='subs',
            name='size',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Order_Number'),
        ),
    ]
