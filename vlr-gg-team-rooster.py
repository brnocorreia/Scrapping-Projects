import requests
import re
from bs4 import BeautifulSoup

url_team = 'https://www.vlr.gg/team/2593/fnatic'
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(url_team, headers = headers)

site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')



player_name_list = site.find_all('div', attrs={'class':'team-roster-item-name-real'})
player_nickname_list = site.find_all('div', attrs={'class':'team-roster-item-name-alias'})

for name, nickname in zip(player_name_list, player_nickname_list):
    player_name = name.text.encode('utf-8').decode('unicode_escape')
    player_nickname = nickname.text.strip().encode('utf-8').decode('unicode_escape')
    print((player_name, player_nickname))



