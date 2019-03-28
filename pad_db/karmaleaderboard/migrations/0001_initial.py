# Generated by Django 2.0.7 on 2019-03-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('link', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RedditUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('scoreUp', models.BooleanField(default=False)),
                ('scoreDown', models.BooleanField(default=False)),
                ('scoreDiff', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TopPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('link', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
