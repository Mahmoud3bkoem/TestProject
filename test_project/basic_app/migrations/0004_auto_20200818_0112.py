# Generated by Django 3.1 on 2020-08-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20200818_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]