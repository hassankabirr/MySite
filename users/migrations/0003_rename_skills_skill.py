# Generated by Django 3.2.7 on 2021-09-24 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210924_2314'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
