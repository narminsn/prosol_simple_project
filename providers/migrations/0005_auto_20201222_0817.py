# Generated by Django 3.1.4 on 2020-12-22 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0004_auto_20201222_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='email',
            new_name='company_email',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='phone',
            new_name='company_phone',
        ),
    ]
