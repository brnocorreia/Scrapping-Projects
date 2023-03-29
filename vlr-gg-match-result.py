import requests
import re
from bs4 import BeautifulSoup

url_player = 'https://www.vlr.gg/184649/team-liquid-brazil-vs-loud-gc-game-changers-2023-brazil-series-1-main-event-gf'
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(url_player, headers = headers)

site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')


# Getting Team A (right side) info #
team_a_info = site.find('div', attrs={'class':'match-header-link-name mod-1'})

team_a_name = team_a_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
team_a_rating = team_a_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

# Getting Team B (left side) info #
team_b_info = site.find('div', attrs={'class':'match-header-link-name mod-2'})

team_b_name = team_b_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
team_b_rating = team_b_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

print(team_a_name, team_a_rating)
print(team_b_name, team_b_rating)

