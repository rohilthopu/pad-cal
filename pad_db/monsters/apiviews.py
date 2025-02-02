from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Monster


class MonsterList(APIView):
    def get(self, request):
        data = Monster.objects.exclude(name__contains='?').exclude(name__contains='*').exclude(
            name__contains='Alt.').values('card_id', 'name', 'active_skill_id', 'leader_skill_id', 'server',
                                          'collab_id', 'series_id')
        return Response(data)


class MonsterObject(APIView):
    def get(self, request, card_id):
        data = Monster.objects.filter(card_id=card_id).values().first()
        return Response(data)
