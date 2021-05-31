from pip._vendor import requests
from bs4 import BeautifulSoup
from classes import battingObj, bowlingObj, fieldingObj

batting_url = 'https://cricclubs.com/EvergreenValleyCricketClub/allBattingRecords.do?league=all&clubId=20865'
html_text = requests.get(batting_url).text
soup = BeautifulSoup(html_text, 'html.parser')
array_range = 50

batting_arr = [ [ None for i in range(18) ] for j in range(array_range) ]

i = 0
array_row = 0
batting_arr[0][0] = 1


for tr in soup.find_all('tr'):
    if i > 5:
        var = 'td'
        if i == 5:
            var = 'th'
        td = tr.find(var)
        
        td_var = tr.find(var)
        array_col = 0
        while td_var is not None:
            batting_arr[array_row][array_col] = td_var.text.strip()
            td_var = td_var.find_next_sibling(var)
            array_col+=1

        array_row+=1

    i+=1

bowling_url = 'https://cricclubs.com/EvergreenValleyCricketClub/allBowlingRecords.do?league=all&clubId=20865'
html_text = requests.get(bowling_url).text
soup = BeautifulSoup(html_text, 'html.parser')

i = 0
array_row = 0
bowling_arr = [ [ None for i in range(16) ] for j in range(array_range) ]
bowling_arr[0][0] = 1

for tr in soup.find_all('tr'):
    if i > 5:
        var = 'td'
        if i == 5:
            var = 'th'
        td = tr.find(var)
        
        td_var = tr.find(var)
        array_col = 0
        while td_var is not None:
            bowling_arr[array_row][array_col] = td_var.text.strip()
            td_var = td_var.find_next_sibling(var)
            array_col+=1

        array_row+=1

    i+=1

fielding_url = 'https://cricclubs.com/EvergreenValleyCricketClub/allFieldingRecords.do?league=all&clubId=20865'
html_text = requests.get(fielding_url).text
soup = BeautifulSoup(html_text, 'html.parser')

i = 0
array_row = 0
fielding_arr = [ [ None for i in range(9) ] for j in range(array_range) ]
fielding_arr[0][0] = 1

for tr in soup.find_all('tr'):
    if i > 5:
        var = 'td'
        if i == 5:
            var = 'th'
        td = tr.find(var)
        
        td_var = tr.find(var)
        array_col = 0
        while td_var is not None:
            fielding_arr[array_row][array_col] = td_var.text.strip()
            td_var = td_var.find_next_sibling(var)
            array_col+=1

        array_row+=1

    i+=1


player_batting = {}
for rows in batting_arr:
    #print(rows)
    player = rows[1]
    #print(player)
    if player is None:
        break
    if player in player_batting:
        print(player + "duplicate entries")
    else:
        playerObj = battingObj(int(rows[0]), rows[1], '', int(rows[2]), int(rows[3]), int(rows[4]), int(rows[5]), int(rows[6]), float(rows[7]), float(rows[8]), int(rows[9]),
                                int(rows[10]), int(rows[11]), int(rows[12]), int(rows[13]), int(rows[14]), int(rows[15]), int(rows[16]))
        player_batting[player] = playerObj

#print(player_batting)
#print(player_batting.values())

#for rows in bowling_arr:
#    player = rows[1]
#    if player is None:
#        break
#    print(rows)


player_bowling = {}
for rows in bowling_arr:
    player = rows[1]
    if player is None:
        break
    overs = float(rows[5])
    balls = int(overs) * 6 + (float(overs) - int(overs)) * 10
    if player in player_bowling:
        print(player + "duplicate entries")
    else:
        playerObj = bowlingObj(int(rows[0]), rows[1], '', int(rows[2]), int(rows[3]), float(rows[4]), int(rows[5]), int(rows[6]), float(rows[7]), float(rows[8]), float(rows[9]),
                                int(rows[10]), int(rows[11]), int(rows[12]), int(rows[13]), int(rows[14]), balls)
        player_bowling[player] = playerObj

#print(player_bowling)

player_fielding = {}
for rows in fielding_arr:
    player = rows[1]
    if player is None:
        break
    if player in player_fielding:
        print(player + "duplicate entries")
    else:
        playerObj = fieldingObj(int(rows[0]), rows[1], '', int(rows[2]), int(rows[3]), int(rows[4]), int(rows[5]), int(rows[6]), int(rows[7]))
        player_fielding[player] = playerObj


print("Batting stats")
count = 0
for value in player_batting.values():
    count+=1
    #print(value)
    player = value.get_player()
    matches = value.get_matches()
    innings = value.get_innings()
    notout = value.get_notout()
    runs = value.get_runs()
    balls = value.get_balls()
    average = '--'
    if (matches - notout) > 0:
        average = runs / (matches - notout)
    strikerate = (runs / balls) * 100
    highscore = value.get_highscore()
    hundreds = value.get_hundreds()
    seventyfive = value.get_seventyfive()
    fifties = value.get_fifties()
    twentyfive = value.get_twentyfive()
    zeros = value.get_zeros()
    fours = value.get_fours()
    sixes = value.get_sixes()

    if average == '--':
        print("%s, %s, %s, %s, %s, %s, %s, %s, %.2f, %s, %s, %s, %s, %s, %s, %s, %s"  % (count, player, matches, innings, notout, runs, balls, average, float(strikerate), highscore, hundreds, seventyfive, fifties, twentyfive, zeros, fours, sixes ))
    else:
        print("%s, %s, %s, %s, %s, %s, %s, %.2f, %.2f, %s, %s, %s, %s, %s, %s, %s, %s"  % (count, player, matches, innings, notout, runs, balls, float(average), float(strikerate), highscore, hundreds, seventyfive, fifties, twentyfive, zeros, fours, sixes ))

print("\nBowling stats")

count = 0
for value in player_bowling.values():
    count+=1
    player = value.get_player()
    matches = value.get_matches()
    innings = value.get_innings()
    overs = value.get_overs()
    balls = value.get_balls()

    overs = (int)(balls / 6) + float ((balls % 6) / 10)
    runs = value.get_runs()
    wickets = value.get_wickets()
    average = 0
    if wickets > 0:
        average = runs / wickets
    
    economy = (runs / balls) * 6
    strikerate = 0.0
    if wickets > 0:
        strikerate = balls / wickets
    hattrick = value.get_hattrick()
    fourwickets = value.get_fourwickets()
    fivewickets = value.get_fivewickets()
    wides = value.get_wides()
    noballs = value.get_noballs()

    print("%s, %s, %s, %s, %s, %s, %s, %.2f, %.2f, %.2f, %s, %s, %s, %s, %s" % (count, player, matches, innings, overs, runs, wickets, average, economy, strikerate, hattrick, fourwickets, fivewickets, wides, noballs))

print("\nFielding stats")

count = 0
for value in player_fielding.values():
    count+=1
    player = value.get_player()
    catches = value.get_catches()
    wkcatches = value.get_wkcatches()
    directro = value.get_directro()
    indirectro = value.get_indirectro()
    stumpings = value.get_stumpings()
    total = value.get_total()

    print("%s, %s, %s, %s, %s, %s, %s, %s" % (count, player, catches, wkcatches, directro, indirectro, stumpings, total))

ranking_url = 'https://cricclubs.com/EvergreenValleyCricketClub/playerRankings.do?clubId=20865'
html_text = requests.get(ranking_url).text
soup = BeautifulSoup(html_text, 'html.parser')

ranking_arr = [ [ None for i in range(10) ] for j in range(array_range) ]

i = 0
array_row = 0
ranking_arr[0][0] = 1


for tr in soup.find_all('tr'):
    if i > 5:
        var = 'td'
        if i == 5:
            var = 'th'
        td = tr.find(var)

        td_var = tr.find(var)
        array_col = 0
        while td_var is not None:
            ranking_arr[array_row][array_col] = td_var.text.strip()
            td_var = td_var.find_next_sibling(var)
            array_col+=1

        array_row+=1

    i+=1

print("\nPlayer Ranking")

count = 0
for rows in ranking_arr:
    count+=1
    player = rows[1]
    if player is None:
        break
    number = rows[0]
    player = rows[1]
    team = rows[2]
    matches = rows[3]
    batting = rows[4]
    bowling = rows[5]
    fielding = rows[6]
    other = rows[7]
    mom = rows[8]
    total = rows[9]

    print("%s, %s, %s, %s, %s, %s, %s, %s, %s" % (count, player, matches, batting, bowling, fielding, other, mom, total))

