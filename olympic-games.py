from collections import Counter
import csv

with open('athlete_events1.csv',mode='r') as csvfile:
    olympic_games_file = csv.DictReader(csvfile)
    teams_silver = set()
    teams_gold = set()
    teams_bronze = set()
    gold_medal_per_team = {}
    goldlist = []
    silverlist = []
    bronzelist = []
    #medal_silver = set()
    #medal_gold = set()
    #medal_bronze = set()
    counter_gold_metals_for_each_team = 0
    counter_for_gold_medals = 0
    counter_for_silver_medals = 0
    counter_for_bronze_medals = 0    
    for row in olympic_games_file:
        team,medal = row["Team"],row["Medal"]
        if medal == "Gold":
            a_list.append(team)
            # for i in a_list:
            #     if team == i:
            #         # counter_gold_metals_for_each_team += 1
            #         gold_medal_per_team[i] =  team  
            teams_gold.add(team)
            #medal_gold.add(medal)
            counter_for_gold_medals += 1
        elif medal =="Silver":    
            teams_silver.add(team)
            #medal_silver.add(medal)
            counter_for_silver_medals += 1
        elif medal == "Bronze":
            teams_bronze.add(team)
            #medal_bronze.add(medal)
            counter_for_bronze_medals += 1
    for key,value in counter_gold_metals_for_each_team.items():
        if value == 1:
            print("The team of %s won %d gold medal!\n" %(key,value))
        else:
            print("The team of %s won %d gold medals!\n" %(key,value))    
    print("The total medals are: %d" %counter_for_gold_medals)
    print(teams_gold)
    print()
    print("gold medals: ",counter_for_gold_medals)
    print()
    print(teams_bronze)
    print("bronze medals: ",counter_for_bronze_medals)
    print()
    print(teams_silver)
    print("silver medals: ",counter_for_silver_medals)

    # txtfile = open('olimpic-games.txt','w')
    # counter_gold_metals_for_each_team = Counter(a_list)
    # for key,value in counter_gold_metals_for_each_team.items():
    #     if value == 1:
    #         txtfile.write("The team of %s won %d gold medal!\n" %(key,value))
    #     else:
    #         txtfile.write("The team of %s won %d gold medals!\n" %(key,value))    
    # txtfile.write("The total medals are: %d" %counter_for_gold_medals)    
    # txtfile.close()
