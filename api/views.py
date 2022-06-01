import json

from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Team
from .serializer import TeamSerializer
import requests
import numpy as np
import joblib


# Create your views here.


@api_view(['GET', 'POST'])
def home(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)

    context = {'teams': teams.order_by('name')}

    print(serializer.data)

    return render(request, 'index.html', context)


@api_view(['GET'])
def get_team(request, team):
    print(team)

    team = Team.objects.get(pk=team)
    serializer = TeamSerializer(team, many=False)

    print(serializer.data)

    return Response({'result': serializer.data})


@api_view(['GET', 'POST'])
@csrf_exempt
def simulation(request):
    print(request)
    data = request.POST['data']
    data = json.loads(data)

    local_team = Team.objects.get(pk=int(data['local_team']))
    print(local_team.name)
    away_team = Team.objects.get(pk=int(data['away_team']))
    print(away_team.name)

    model = open('modelo.pkl', 'rb')

    tree = joblib.load(model)

    local_team_stats = np.array([local_team.shots,
                                 local_team.shots_on_target,
                                 local_team.fouls_committed,
                                 local_team.corner,
                                 local_team.yellow_card,
                                 local_team.red_card, ])/local_team.match

    away_team_stats = np.array([away_team.shots,
                                away_team.shots_on_target,
                                away_team.fouls_committed,
                                away_team.corner,
                                away_team.yellow_card,
                                away_team.red_card, ])/away_team.match

    print('Partidos del equipo local', local_team.match)
    print('Partidos del equipo visitante', away_team.match)

    print('Estadisticas locales', local_team_stats)
    print("Estadisticas visitante", away_team_stats)

    draft = np.append(local_team_stats, away_team_stats)
    print('Partido', draft)

    result = tree.predict(draft.reshape(1, -1))
    print('resultado', result)

    if result == 0:
        return Response({'result': result, 'team': local_team.name})
    elif result == 1:
        return Response({'result': result, 'team': away_team.name})
    else:
        return Response({'result': result, 'team': 'Empate'})

