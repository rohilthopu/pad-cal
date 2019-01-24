# Generated by Django 2.0.7 on 2019-01-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('dungeonID', models.IntegerField(default=0)),
                ('startTime', models.FloatField(default=0)),
                ('endTime', models.FloatField(default=0)),
                ('bonusName', models.CharField(default='', max_length=100)),
                ('bonusStart', models.FloatField(default=0)),
                ('bonusEnd', models.FloatField(default=0)),
            ],
        ),
    ]
