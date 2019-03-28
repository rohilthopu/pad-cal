# Generated by Django 2.0.7 on 2019-03-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnemySkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('effect', models.TextField(default='')),
                ('enemy_skill_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeSkillID', models.IntegerField(blank=True, default=0)),
                ('ancestorID', models.IntegerField(default=0)),
                ('attributeID', models.IntegerField(default=0)),
                ('attribute', models.CharField(default='', max_length=100)),
                ('awakenings', models.TextField(default='')),
                ('awakenings_raw', models.TextField(default='')),
                ('baseID', models.IntegerField(default=0)),
                ('cardID', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('inheritable', models.CharField(default='', max_length=5)),
                ('isCollab', models.CharField(default='', max_length=5)),
                ('isReleased', models.CharField(default='', max_length=5)),
                ('isUlt', models.CharField(default='', max_length=5)),
                ('leaderSkillID', models.IntegerField(blank=True, default=0)),
                ('maxATK', models.IntegerField(default=0)),
                ('maxHP', models.IntegerField(default=0)),
                ('maxLevel', models.IntegerField(default=0)),
                ('maxRCV', models.IntegerField(default=0)),
                ('minATK', models.IntegerField(default=0)),
                ('minHP', models.IntegerField(default=0)),
                ('minRCV', models.IntegerField(default=0)),
                ('maxXP', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=200)),
                ('rarity', models.IntegerField(default=0)),
                ('subAttributeID', models.IntegerField(default=0)),
                ('subattribute', models.CharField(default='', max_length=100)),
                ('hp99', models.IntegerField(default=0)),
                ('atk99', models.IntegerField(default=0)),
                ('rcv99', models.IntegerField(default=0)),
                ('superAwakenings', models.TextField(default='')),
                ('superAwakenings_raw', models.TextField(default='')),
                ('evos_raw', models.TextField(default='')),
                ('evomat1', models.IntegerField(default=0)),
                ('evomat2', models.IntegerField(default=0)),
                ('evomat3', models.IntegerField(default=0)),
                ('evomat4', models.IntegerField(default=0)),
                ('evomat5', models.IntegerField(default=0)),
                ('unevomat1', models.IntegerField(default=0)),
                ('unevomat2', models.IntegerField(default=0)),
                ('unevomat3', models.IntegerField(default=0)),
                ('unevomat4', models.IntegerField(default=0)),
                ('unevomat5', models.IntegerField(default=0)),
                ('type1', models.CharField(default='', max_length=100)),
                ('type2', models.CharField(default='', max_length=100)),
                ('type3', models.CharField(default='', max_length=100)),
                ('sellMP', models.IntegerField(default=0)),
                ('sellCoin', models.IntegerField(default=0)),
                ('enemy_skills', models.TextField(default='')),
                ('server', models.CharField(default='', max_length=2)),
                ('evolutions', models.ManyToManyField(to='monsterdatabase.Evolution')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(default=-1)),
                ('skill_type', models.CharField(default='', max_length=50)),
                ('hp_mult', models.FloatField(default=1)),
                ('atk_mult', models.FloatField(default=1)),
                ('rcv_mult', models.FloatField(default=1)),
                ('dmg_reduction', models.FloatField(default=0)),
                ('c_skill_1', models.IntegerField(default=-1)),
                ('c_skill_2', models.IntegerField(default=-1)),
                ('c_skill_3', models.IntegerField(default=-1)),
                ('skill_class', models.CharField(default='', max_length=100)),
                ('levels', models.IntegerField(default=0)),
                ('maxTurns', models.IntegerField(blank=True, default=0)),
                ('minTurns', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
