from collections import Counter
import csv,re

with open('athlete_events.csv',mode='r') as csvfile:
    olympic_games_file = csv.DictReader(csvfile)
    teams_silver = set()
    teams_gold = set()
    teams_bronze = set()
    goldlist = []
    silverlist = []
    bronzelist = []
    counter_gold_metals_for_each_team = 0
    counter_silver_metals_for_each_team = 0
    counter_bronze_metals_for_each_team = 0
    counter_for_gold_medals = 0
    counter_for_silver_medals = 0
    counter_for_bronze_medals = 0    
    for row in olympic_games_file:
        team,medal = row["Team"],row["Medal"]
        if medal == "Gold":
            goldlist.append(team)
            teams_gold.add(team)
            # teams_gold = [re.sub('[-0-9]', '', item) for item in teams_gold]
            counter_for_gold_medals += 1
        elif medal =="Silver":
            silverlist.append(team)
            teams_silver.add(team)
            counter_for_silver_medals += 1
        elif medal == "Bronze":
            bronzelist.append(team)    
            teams_bronze.add(team)
            counter_for_bronze_medals += 1
    goldlist = [re.sub('[-0-9]', '', item) for item in goldlist]
    silverlist = [re.sub('[-0-9]', '', item) for item in silverlist] 
    bronzelist = [re.sub('[-0-9]', '', item) for item in bronzelist]       
    counter_gold_metals_for_each_team = Counter(goldlist)
    counter_silver_metals_for_each_team = Counter(silverlist)
    counter_bronze_metals_for_each_team = Counter(bronzelist)        
    for key,value in counter_gold_metals_for_each_team.items():
        if value == 1:
            print("The team of %s won %d gold medal!\n" %(key,value))
        else:
            print("The team of %s won %d gold medals!\n" %(key,value))
    print("The total medals are: %d" %counter_for_gold_medals)                        
    print("The list with teams that won gold medals: \n",teams_gold)
    print()
    print()         
    for key,value in counter_silver_metals_for_each_team.items():
        if value == 1:
            print("The team of %s won %d silver medal!\n" %(key,value))
        else:
            print("The team of %s won %d silver medals!\n" %(key,value))        
    print("The total medals are: %d" %counter_for_silver_medals)
    print("The list with teams that won silver medals: \n",teams_silver)
    print()
    print()        
    for key,value in counter_bronze_metals_for_each_team.items():
        if value == 1:
            print("The team of %s won %d bronze medal!\n" %(key,value))
        else:
            print("The team of %s won %d bronze medals!\n" %(key,value))      
    print("The total medals are: %d" %counter_for_bronze_medals)
print("The list with teams that won bronze medals: \n",teams_bronze)
