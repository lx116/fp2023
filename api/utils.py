import requests
from .models import Team


def get_league_by_name(league):
    pass


def get_team_data(team):
    API_TOKEN = 'BEUVFKDl0MMlHcU2qEUEBvtU0C3664pYjOaKbgCxPOzcNCV6uuNeu7HEiBC2'

    url = f'https://soccer.sportmonks.com/api/v2.0/teams/{team}?api_token={API_TOKEN}&include=stats&seasons=18378'

    response = requests.request("GET", url)

    data = response.json()

    team = Team()
    team.name = data['data']['name']
    team.logo = data['data']['logo_path']
    team.shots = data["data"]["stats"]["data"][0]["shots_on_target"] + data["data"]["stats"]["data"][0]["shots_off_target"]
    team.shots_on_target = data["data"]["stats"]["data"][0]["shots_on_target"]
    team.red_card = data["data"]['stats']['data'][0]['redcards']
    team.yellow_card = data["data"]["stats"]["data"][0]["yellowcards"]
    team.fouls_committed = data["data"]["stats"]["data"][0]["fouls"]
    team.corner = data["data"]["stats"]["data"][0]["total_corners"]
    team.match = 38

    team.save()

