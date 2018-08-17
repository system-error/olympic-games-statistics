from collections import Counter
import csv,re,time
from itertools import chain
import matplotlib.pyplot as plt
import numpy as np
start = time.time()

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
    teams_gold = set([re.sub('[-0-9]', '', s) for s in teams_gold]) 
    teams_silver = set([re.sub('[-0-9]', '', s) for s in teams_silver])
    teams_bronze = set([re.sub('[-0-9]', '', s) for s in teams_bronze])      
    counter_gold_metals_for_each_team = Counter(goldlist)
    counter_silver_metals_for_each_team = Counter(silverlist)
    counter_bronze_metals_for_each_team = Counter(bronzelist)        
    for gold_key,gold_value in counter_gold_metals_for_each_team.items():
        if gold_value == 1:
            print("The team of %s won %d gold medal!\n" %(gold_key,gold_value))
        else:
            print("The team of %s won %d gold medals!\n" %(gold_key,gold_value))
    print("The total medals are: %d" %counter_for_gold_medals)                        
    print("The list with teams that won gold medals: \n",teams_gold)
    print()
    print()         
    for silver_key,silver_value in counter_silver_metals_for_each_team.items():
        if silver_value == 1:
            print("The team of %s won %d silver medal!\n" %(silver_key,silver_value))
        else:
            print("The team of %s won %d silver medals!\n" %(silver_key,silver_value))        
    print("The total medals are: %d" %counter_for_silver_medals)
    print("The list with teams that won silver medals: \n",teams_silver)
    print()
    print()        
    for bronze_key,bronze_value in counter_bronze_metals_for_each_team.items():
        if bronze_value == 1:
            print("The team of %s won %d bronze medal!\n" %(bronze_key,bronze_value))
        else:
            print("The team of %s won %d bronze medals!\n" %(bronze_key,bronze_value))      
    print("The total medals are: %d" %counter_for_bronze_medals)
print("The list with teams that won bronze medals: \n",teams_bronze)

print()
print()
print()

#b = set(chain(teams_gold,teams_silver,teams_bronze))
#total = len(b)

legend = ['Gold Medals For Each Team','Silver Medals For Each Team','Bronze Medals For Each Team']
plt.hist([goldlist,silverlist,bronzelist], color=['orange','green','red'])
plt.xlabel("List With Teams")
plt.ylabel("Gold Medals For Each Team")
plt.legend(legend)
# plt.xticks(range(0,bins))
# plt.yticks(range(1, gold_value))
# plt.yticks(range(1, silver_value))
# plt.yticks(range(1, bronze_value))
# plt.savefig("abc.png")
plt.show()

print ('It took', time.time()-start, 'seconds.')
