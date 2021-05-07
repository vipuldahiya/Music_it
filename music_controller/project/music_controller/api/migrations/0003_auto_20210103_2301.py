# Generated by Django 3.1.4 on 2021-01-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210101_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_song',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='WL0ofbsP', max_length=8, unique=True),
        ),
    ]
