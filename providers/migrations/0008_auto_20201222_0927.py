# Generated by Django 3.1.4 on 2020-12-22 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0007_auto_20201222_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providercontact',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.provider'),
        ),
    ]
