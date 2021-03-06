# Generated by Django 3.0.5 on 2020-04-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0020_auto_20200423_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='contact',
            field=models.IntegerField(max_length=50, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='friends',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='Email id'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='photo',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Profile Picture,'),
        ),
    ]
