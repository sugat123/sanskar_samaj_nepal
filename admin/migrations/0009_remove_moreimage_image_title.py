# Generated by Django 2.2 on 2019-06-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0008_sectioncomponent_login_bg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moreimage',
            name='image_title',
        ),
    ]
