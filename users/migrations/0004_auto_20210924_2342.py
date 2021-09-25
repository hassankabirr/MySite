# Generated by Django 3.2.7 on 2021-09-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_skills_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_stackoverflow',
        ),
        migrations.AddField(
            model_name='profile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
