# Generated by Django 3.1.1 on 2022-02-17 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20220217_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
