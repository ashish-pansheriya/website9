# Generated by Django 3.0.5 on 2020-04-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200423_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='databank',
            name='category',
            field=models.CharField(choices=[('01', 'Buy & Sell'), ('02', 'Cars & Vehicles'), ('03', 'Real Estate'), ('04', 'Mobiles'), ('05', 'Furniture'), ('06', 'Bikes'), ('07', 'Jobs'), ('08', 'Services'), ('09', 'Community'), ('10', 'Vacation Rentals')], max_length=20, null=True, verbose_name='Select a category'),
        ),
        migrations.AlterField(
            model_name='databank',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='databank',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Ad title'),
        ),
    ]
