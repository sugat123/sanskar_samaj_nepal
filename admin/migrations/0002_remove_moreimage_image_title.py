# Generated by Django 2.2 on 2019-06-04 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moreimage',
            name='image_title',
        ),
    ]
