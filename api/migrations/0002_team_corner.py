# Generated by Django 4.0.4 on 2022-05-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='corner',
            field=models.FloatField(default=0),
        ),
    ]