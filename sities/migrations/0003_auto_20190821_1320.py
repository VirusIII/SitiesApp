# Generated by Django 2.2.4 on 2019-08-21 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sities', '0002_auto_20190821_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city_name',
            new_name='name',
        ),
    ]
