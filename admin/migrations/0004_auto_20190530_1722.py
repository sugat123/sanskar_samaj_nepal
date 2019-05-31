# Generated by Django 2.2 on 2019-05-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_auto_20190530_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='about_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='setting'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook_link',
            field=models.URLField(blank=True, default='https://www.facebook.com', null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='insta_link',
            field=models.URLField(blank=True, default='https://www.instagram.com', null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='setting'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter_link',
            field=models.URLField(blank=True, default='https://www.twitter.com', null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='volunteer_bg_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='setting'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='volunteer_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='setting'),
        ),
    ]
