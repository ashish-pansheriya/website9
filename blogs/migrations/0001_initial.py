# Generated by Django 3.0.5 on 2020-05-15 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blogbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Blog title')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Your Name')),
                ('category', models.CharField(choices=[('Fashion Blog', 'Fashion Blog'), ('Food Blog', 'Food Blog'), ('Travel Blog', 'Travel Blog'), ('Music Blog', 'Music Blog'), ('Lifestyle Blog', 'Lifestyle Blog'), ('Fitness Blog', 'Fitness Blog'), ('DIY Blog', 'DIY Blog'), ('Sports Blog', 'Sports Blog'), ('Finance Blog', 'Finance Blog'), ('Political Blog', 'Political Blog'), ('Parenting Blog', 'Parenting Blog'), ('Business Blog', 'Business Blog'), ('Personal Blog', 'Personal Blog'), ('Movie Blog', 'Movie Blog'), ('Car Blog', 'Car Blog'), ('News Blog', 'News Blog'), ('Pet Blog', 'Pet Blog'), ('Gaming Blog', 'Gaming Blog'), ('Technology Blog', 'Technology Blog'), ('Religious Blog', 'Religious Blog'), ('Story Blog', 'Story Blog'), ('Blog', 'Blog')], default='Blog', max_length=20, null=True, verbose_name='Your Blog About')),
                ('content', models.TextField(max_length=400, null=True, verbose_name='Description')),
                ('photo', models.ImageField(upload_to='media', verbose_name='Blog Image')),
                ('location', models.CharField(max_length=100, null=True, verbose_name='Location')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Posted')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
    ]
