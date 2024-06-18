import requests
import json

'''

uri = 'https://api.football-data.org/v4/competitions/PL/scorers'
headers = { 'X-Auth-Token': '15cd8b6230734db5ba0f5f6fe511616f' }

response = requests.get(uri, headers=headers)

block = response.json()

for player in block["scorers"]:
    print(f" the player name is {player["player"]["name"]} and they play for {player["team"]["name"]}")
    
    
    
'''
uri = 'https://api.football-data.org/v4/competitions/PL/scorers'
headers = { 'X-Auth-Token': '15cd8b6230734db5ba0f5f6fe511616f' }

response = requests.get(uri, headers=headers)

block = response.json()

for player in block["scorers"]:
    print(player["player"]["name"])










'''
uri = "https://api.football-data.org/v4/competitions/PL/standings"
team_names = []
for standing in response.json()['standings']:
    for team_entry in standing['table']:
        team_names.append(team_entry['team']['name'])

for name in team_names:
    print(name)

#print(json.dumps(response.json(),indent=2))

'''
