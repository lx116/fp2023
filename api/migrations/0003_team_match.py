# Generated by Django 4.0.4 on 2022-06-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_team_corner'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='match',
            field=models.IntegerField(default=0),
        ),
    ]
