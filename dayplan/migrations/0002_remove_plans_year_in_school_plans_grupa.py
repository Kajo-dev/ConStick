# Generated by Django 4.0.3 on 2022-04-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayplan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='plans',
            name='grupa',
            field=models.CharField(choices=[('OS', 'osobiste'), ('PR', 'praca')], default='OS', max_length=2),
        ),
    ]
