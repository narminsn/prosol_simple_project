# Generated by Django 3.1.4 on 2020-12-22 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0013_auto_20201222_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providercontact',
            name='provider',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.provider'),
        ),
        migrations.AlterField(
            model_name='serviceinformation',
            name='provider',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.provider'),
        ),
    ]
