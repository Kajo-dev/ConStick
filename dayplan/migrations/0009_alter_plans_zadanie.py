# Generated by Django 4.0.3 on 2022-04-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayplan', '0008_plans_zadanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='zadanie',
            field=models.CharField(default='', max_length=20),
        ),
    ]
