# Generated by Django 3.1.1 on 2022-03-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_remove_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bed_room',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]