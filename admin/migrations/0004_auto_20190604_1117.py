# Generated by Django 2.2 on 2019-06-04 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_moreimage_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreimage',
            name='image_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.Gallery'),
        ),
    ]
