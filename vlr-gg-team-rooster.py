import requests
import re
from bs4 import BeautifulSoup

url_team = 'https://www.vlr.gg/team/6961/loud'
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(url_team, headers = headers)

site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

player_name_list = site.find_all('div', attrs={'class':'team-roster-item-name-real'})
player_nickname_list = site.find_all('div', attrs={'class':'team-roster-item-name-alias'})

for name, nickname in zip(player_name_list, player_nickname_list):
    player_name = name.text.strip().encode('utf-8').decode('unicode_escape')
    player_nickname = nickname.text.strip().encode('utf-8').decode('unicode_escape')

    # Verificar se a div existe
    name_div = name.find_parent('div', {'class': 'team-roster-item-name'})
    role_div = name_div.find('div', {'class': 'wf-tag mod-light team-roster-item-name-role'})
    
    if role_div is not None:
        role = role_div.text.strip().encode('utf-8').decode('unicode_escape')
        print('Name: ' + player_name)
        print('Nickname: ' + player_nickname)
        print('Role: ' + role.title())
        print('\n')
    else:
        print('Name: ' + player_name)
        print('Nickname: ' + player_nickname)
        print('Role: Player')
        print('\n')
