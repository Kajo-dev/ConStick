# Generated by Django 4.0.3 on 2022-04-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayplan', '0007_alter_plans_zrobione'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='zadanie',
            field=models.TextField(default=''),
        ),
    ]