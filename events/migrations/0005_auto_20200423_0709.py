# Generated by Django 3.0.5 on 2020-04-23 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20200423_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='organiser',
            field=models.CharField(max_length=200, null=True, verbose_name='Organiser Name'),
        ),
        migrations.AlterField(
            model_name='events',
            name='author',
            field=models.ForeignKey(max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='events',
            name='description2',
            field=models.CharField(max_length=200, null=True, verbose_name='Organiser Description'),
        ),
        migrations.AlterField(
            model_name='events',
            name='tickets',
            field=models.CharField(max_length=50, null=True, verbose_name='Tickets info'),
        ),
        migrations.AlterField(
            model_name='events',
            name='types',
            field=models.CharField(choices=[('01', 'Select the type of event'), ('02', 'Appearance or Signing'), ('03', 'Attraction'), ('04', 'Camp, Trip or Retreat'), ('05', 'Concert or Performance'), ('06', 'Conference'), ('07', 'Course, Training or Workshop'), ('08', 'Dinner or Gala'), ('09', 'Festival or Fair'), ('10', 'Meeting or Networking Event'), ('11', 'Party or Social Gathering'), ('12', 'Race or Endurance Event'), ('13', 'Tournament'), ('14', 'Rally'), ('15', 'Seminar or Talk'), ('16', 'Tour'), ('17', 'Tradeshow, Consumer Show..')], max_length=50, null=True, verbose_name='Event Type'),
        ),
    ]
