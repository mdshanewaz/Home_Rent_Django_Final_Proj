# Generated by Django 3.1.1 on 2022-03-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0046_auto_20220321_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
