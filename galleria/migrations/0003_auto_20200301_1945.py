# Generated by Django 3.0.3 on 2020-03-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0002_auto_20200301_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
    ]