# Generated by Django 4.2.7 on 2023-12-03 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_site',
            new_name='portfolio_site',
        ),
    ]
