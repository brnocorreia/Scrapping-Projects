import requests
import re
from bs4 import BeautifulSoup

url_player = 'https://www.vlr.gg/184649/team-liquid-brazil-vs-loud-gc-game-changers-2023-brazil-series-1-main-event-gf'
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(url_player, headers = headers)
site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

# Getting event and match info (event name) #
event_info = site.find('div', attrs={'class':'match-header-super'})
event_name = event_info.find('div', attrs={'style':'font-weight: 700;'}).text.strip()

print(event_name)

# Getting Date and Hour #
match_start = site.find('div', attrs={'class':'match-header-date'})

match_date = match_start.find('div', attrs={'data-moment-format':'dddd, MMMM Do'}).text.strip()
match_hour = match_start.find('div', attrs={'data-moment-format':'h:mm A z'}).text.strip()

print(match_date + ' - ' + match_hour + ' GMT')

# Getting match score #
score_param = site.find('span', attrs={'class':'match-header-vs-score-colon'})
score_team_a = score_param.find_previous().text.strip()
score_team_b = score_param.find_next().text.strip()

# Getting Team A (right side) info #
team_a_info = site.find('div', attrs={'class':'match-header-link-name mod-1'})

team_a_name = team_a_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
team_a_rating = team_a_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

# Getting Team B (left side) info #
team_b_info = site.find('div', attrs={'class':'match-header-link-name mod-2'})

team_b_name = team_b_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
team_b_rating = team_b_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

# Printing match header with name, rating and score #
print(team_a_name, team_a_rating, score_team_a + ' x ' + score_team_b, team_b_rating, team_b_name)

# Getting Picks and Bans info #

picks_bans = site.find('div', attrs={'class':'match-header-note'}).text.strip()

print(picks_bans)





