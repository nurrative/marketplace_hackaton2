# Generated by Django 4.2 on 2023-05-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
    ]
