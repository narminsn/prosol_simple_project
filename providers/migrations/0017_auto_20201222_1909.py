# Generated by Django 3.1.4 on 2020-12-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0016_auto_20201222_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='company_email',
            field=models.EmailField(max_length=100),
        ),
    ]