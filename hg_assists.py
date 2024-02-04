from bs4 import BeautifulSoup
from urllib.request import urlopen

teams = {'hawks': 'ATL', 'celtics': 'BOS', 'nets': 'BRK', 'hornets': 'CHA', 'bulls': 'CHI', 'cavs': 'CLE', 
         'mavs': 'DAL', 'nuggets': 'DEN', 'pistons': 'DET', 'warriors': 'GSW', 'rockets': 'HOU', 
         'pacers': 'IND', 'clippers': 'LAC', 'lakers': 'LAL', 'grizzlies': 'MEM', 'heat': 'MIA', 'bucks': 'MIL',
         'wolves': 'MIN', 'pelicans': 'NOH', 'knicks': 'NYK', 'thunder': 'OKC', 'magic': 'ORL', 
         'sixers': 'PHI', 'suns': 'PHO', 'blazers': 'POR', 'kings': 'SAC', 'spurs': 'SAS', 'raptors': 'TOR', 
         'jazz': 'UTA', 'wizards': 'WAS'}

print('\nEnter teams as shown below. If entering a player name, do not use special characters.')
print('Combine hyphenated or multiple first and last names. Enter everything in lower case.')
print('ex. J.J. Redick = jj redick, Karl-Anthony Towns = karlanthony towns, Luc Mbah A Moute = luc mbahamoute')
print('*Disclaimer: due to some players having the same name, list of teammates may not be accurate')
print('\nTeams: ')
print('hawks, celtics, nets, hornets, bulls, cavs, mavs, nuggets, pistons, warriors, rockets, pacers,')
print('clippers, lakers, grizzlies, heat, bucks, wolves, pelicans, knicks, thunder, magic, sixers,')
print('suns, blazers, kings, spurs, raptors, jazz, wizards\n')


q1 = input('Team or teammate?: ')
if q1 == 'team':
    inp1 = input('Enter team: ')
    url1 = 'https://www.basketball-reference.com/teams/' + teams.get(inp1) + '/players.html'
else: 
    inp1 = input('Enter player: ')
    player1 = inp1.split()
    player1[0] = player1[0][0:2]
    player1[1] = player1[1][0:5]
    player1 = player1[1] + player1[0]
    url1 = 'https://www.basketball-reference.com/friv/teammates_and_opponents.fcgi?pid=' + player1 + '01&type=t'

q2 = input("Team or teammate?: ")
if q2 == 'team':
    inp2 = input('Enter team: ')
    url2 = 'https://www.basketball-reference.com/teams/' + teams.get(inp2) + '/players.html'
else: 
    inp2 = input('Enter player: ')
    player2 = inp2.split()
    player2[0] = player2[0][0:2]
    player2[1] = player2[1][0:5]
    player2 = player2[1] + player2[0]
    url2 = 'https://www.basketball-reference.com/friv/teammates_and_opponents.fcgi?pid=' + player2 + '01&type=t'

html1 = urlopen(url1)
html2 = urlopen(url2)

soup1 = BeautifulSoup(html1, features="lxml")
soup2 = BeautifulSoup(html2, features="lxml")

rows1 = soup1.findAll('tr')[2:]
rows_data1 = [[td.getText() for td in rows1[i].findAll('td')]
                    for i in range(len(rows1))]
rows2 = soup2.findAll('tr')[2:]
rows_data2 = [[td.getText() for td in rows2[i].findAll('td')]
                    for i in range(len(rows2))]

rows_data1 = [ele for ele in rows_data1 if ele != []]
rows_data2 = [ele for ele in rows_data2 if ele != []]

names1 = [''] * len(rows_data1)
for i in range(len(rows_data1)):
    names1[i] = rows_data1[i][0].replace('*', '')
names2 = [''] * len(rows_data2)
for i in range(len(rows_data2)):
    names2[i] = rows_data2[i][0].replace('*', '')

common_players = []
for i in range(len(names1)):
    if names1[i] in names2:
        common_players.append(names1[i])

print('\nCommon players: ')
print(common_players)
