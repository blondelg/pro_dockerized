# Generated by Django 2.2.11 on 2020-06-21 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0002_auto_20200621_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]