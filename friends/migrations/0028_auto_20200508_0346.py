# Generated by Django 3.0.5 on 2020-05-08 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0027_auto_20200508_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='photo',
            new_name='file',
        ),
    ]
