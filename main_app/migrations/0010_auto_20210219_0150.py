# Generated by Django 3.1.6 on 2021-02-19 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210219_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/%Y/%m/'),
        ),
    ]