from django.core.management.base import BaseCommand, CommandError
from monsterdatabasejp.models import Skill
import requests
import json
import time

from .skill_parser import parse_skill_multiplier, Multiplier
from .skill_type_maps import SKILL_TYPE


class Command(BaseCommand):
    help = 'Runs an update on the models to add to the database.'

    def handle(self, *args, **options):

        Skill.objects.all().delete()

        link = 'https://storage.googleapis.com/mirubot/paddata/raw/jp_skills.json'

        req = requests.get(link).text
        data = json.loads(req)

        print()
        print("Updating skill list.")
        print()
        start = time.time()

        for item in data:

            if item['skill_id'] != 0:

                # if not allSkills.filter(skillID=item['skill_id']).exists():

                    skill = Skill()
                    skill.name = item['name']
                    skill.description = item['clean_description']
                    skill.skillID = item['skill_id']

                    if item['levels'] is not None:
                        skill.levels = item['levels']
                        skill.maxTurns = item['turn_max']
                        skill.minTurns = item['turn_min']
                        skill.skill_type = "active"
                    else:
                        skill.skill_type = "leader"

                    skill_type = item['skill_type']
                    other_fields = item['other_fields']

                    skill.skill_class = SKILL_TYPE[skill_type]

                    try:
                        multipliers = parse_skill_multiplier(skill_type, other_fields, len(other_fields))
                    except Exception as e:
                        print('skill parsing failed for', other_fields, 'with exception:', e)
                        print('Skill:', item)
                        multipliers = Multiplier()

                    skill.hp_mult = multipliers.hp
                    skill.atk_mult = multipliers.atk
                    skill.rcv_mult = multipliers.rcv
                    skill.dmg_reduction = multipliers.shield

                    if skill_type == 116 or skill_type == 138:
                        skill.c_skill_1 = other_fields[0]
                        skill.c_skill_2 = other_fields[1]
                        if len(other_fields) == 3:
                            skill.c_skill_3 = other_fields[2]

                    skill.save()

        end = time.time()
        print()
        print("Elapsed time:", end-start, "s")
        print()

