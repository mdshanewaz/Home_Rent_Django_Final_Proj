# Generated by Django 3.1.1 on 2022-03-11 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_remove_post_rent_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Location',
        ),
    ]
