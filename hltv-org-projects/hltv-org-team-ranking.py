import requests
from bs4 import BeautifulSoup
import re

ranking_url = input('Insert the ranking URL to continue: ')
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(ranking_url, headers = headers)
site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

teams = site.find_all('div', attrs={'class':'ranked-team standard-box'})


for team in teams:
    team_ranking = team.find('span', attrs={'class':'position'}).text
    print(team_ranking)
    print()

