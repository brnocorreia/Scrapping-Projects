import requests
import re
from bs4 import BeautifulSoup

url_player = input('Insert the match URL on vlr.gg to continue: ')
headers = {'user-agent':'Mozilla/5.0'}

response = requests.get(url_player, headers = headers)
site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

if site.find('span', attrs={'class':'match-header-vs-note mod-live'}) is None:

    # Getting event and match info (event name) #
    event_info = site.find('div', attrs={'class':'match-header-super'})
    event_name = event_info.find('div', attrs={'style':'font-weight: 700;'}).text.strip()

    print(event_name)
    print('\n')

    # Getting Date and Hour #
    match_start = site.find('div', attrs={'class':'match-header-date'})

    match_date = match_start.find('div', attrs={'data-moment-format':'dddd, MMMM Do'}).text.strip()
    match_hour = match_start.find('div', attrs={'data-moment-format':'h:mm A z'}).text.strip()

    print(match_date + ' | ' + match_hour + ' GMT')
    print('\n')

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
    print('\n')

    # Getting Picks and Bans info #

    picks_bans = site.find('div', attrs={'class':'match-header-note'}).text.strip()

    print('Picks and Bans: ' + picks_bans)
    print('\n')

    # Getting every map score (map1, map2, map3 and etc) #
    matches = site.find_all('div', attrs={'class':'vm-stats-game-header'})
    map_list = site.find_all('span', attrs={'style':'position: relative;'})

    teamA_mapscores = site.find_all('div', attrs={'class':'team'})
    teamB_mapscores = site.find_all('div', attrs={'class':'team mod-right'})

    map_names = []

    for map in map_list:
        map_name = map.contents[0].strip()
        map_names.append(map_name)


    i = 0

    for match in matches:
        teamA = match.find('div', class_='team')
        teamB = match.find('div', class_='team mod-right')
        i = i

        
        if teamA.find('div', class_='score mod-win') is not None and teamB.find('div', class_='score mod-win') is None:

            mapscore_a = teamA.find('div', attrs={'class':'score mod-win'}).text.strip()
            mapscore_a_ct = teamA.find('span', attrs={'class':'mod-ct'}).text.strip()
            mapscore_a_t = teamA.find('span', attrs={'class':'mod-t'}).text.strip()
            mapscore_b = teamB.find('div', attrs={'class':'score'}).text.strip()
            mapscore_b_ct = teamB.find('span', attrs={'class':'mod-ct'}).text.strip()
            mapscore_b_t = teamB.find('span', attrs={'class':'mod-t'}).text.strip()

            mapscore_a_halfs = (' [Def: ' + mapscore_a_ct + ' | Atk: ' + mapscore_a_t + '] ')
            mapscore_b_halfs = (' [Def: ' + mapscore_b_ct + ' | Atk: ' + mapscore_b_t + '] ')

            print('Map: ' + map_names[i] + ' | ' + team_a_name + ' ' + mapscore_a_halfs +mapscore_a + ' x ' + mapscore_b + mapscore_b_halfs + ' ' + team_b_name)
            # for mapscore_teamA, mapscore_teamB in zip(teamA_mapscores,teamB_mapscores):
            #     mapscore_a = mapscore_teamA.find('div', attrs={'class':'score mod-win'})
            #     mapscore_b = mapscore_teamB.find('div', attrs={'class':'score'})
            #     print(mapscore_a, '  | ', mapscore_b)
            #     print('team a venceu')
            i += 1
            
        else: 
            
            mapscore_a = teamA.find('div', attrs={'class':'score'}).text.strip()
            mapscore_a_ct = teamA.find('span', attrs={'class':'mod-ct'}).text.strip()
            mapscore_a_t = teamA.find('span', attrs={'class':'mod-t'}).text.strip()
            mapscore_b = teamB.find('div', attrs={'class':'score mod-win'}).text.strip()
            mapscore_b_ct = teamB.find('span', attrs={'class':'mod-ct'}).text.strip()
            mapscore_b_t = teamB.find('span', attrs={'class':'mod-t'}).text.strip()

            mapscore_a_halfs = (' [Def: ' + mapscore_a_ct + ' | Atk: ' + mapscore_a_t + '] ')
            mapscore_b_halfs = (' [Def: ' + mapscore_b_ct + ' | Atk: ' + mapscore_b_t + '] ')

            print('Map: ' + map_names[i] + ' | ' + team_a_name + ' ' + mapscore_a_halfs +mapscore_a + ' x ' + mapscore_b + mapscore_b_halfs + ' ' + team_b_name)
            # if teamA.find('div', class_='score mod-win') is not None and teamB.find('div', class_='score mod-win') is None:

            # for mapscore_teamA, mapscore_teamB in zip(teamA_mapscores,teamB_mapscores):
            #         mapscore_a = mapscore_teamA.find('div', attrs={'class':re.compile('score')})
            #         mapscore_b = mapscore_teamB.find('div', attrs={'class':re.compile('score mod-win')})
            #         print(mapscore_a, '  | ', mapscore_b)
            #         print('team b venceu')

            i += 1
else: 
    print('The match is not over yet, currently [LIVE]. We support only finished matches.')