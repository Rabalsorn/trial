# Generated by Django 5.0.3 on 2024-04-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0002_datachange_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='datachange',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
