# Generated by Django 3.1.4 on 2020-12-23 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0021_auto_20201222_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providercontact',
            name='rol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]