# Generated by Django 3.1.6 on 2021-02-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210219_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
