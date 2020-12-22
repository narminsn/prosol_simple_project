# Generated by Django 3.1.4 on 2020-12-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0020_auto_20201222_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceinformation',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Waiting'), ('1', 'Approve'), ('2', 'Cancel')], default='0', max_length=40),
        ),
    ]