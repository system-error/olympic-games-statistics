import csv

with open('athlete_events.csv',mode='r') as csvfile:
    olympic_games_file = csv.DictReader(csvfile)
    teams_silver = set()
    teams_gold = set()
    teams_bronze = set()
    medal_silver = set()
    medal_gold = set()
    medal_bronze = set()
    counter_for_gold_medals = 0
    counter_for_silver_medals = 0
    counter_for_bronze_medals = 0    
    for row in olympic_games_file:
        team,medal = row["Team"],row["Medal"]
        if medal =="Gold":    
            teams_gold.add(team)
            medal_gold.add(medal)
            counter_for_gold_medals += 1
        elif medal =="Silver":    
            teams_silver.add(team)
            medal_silver.add(medal)
            counter_for_silver_medals += 1
        elif medal == "Bronze":
            teams_bronze.add(team)
            medal_bronze.add(medal)
            counter_for_bronze_medals += 1
    print(teams_gold)
    print("gold medals: ",counter_for_gold_medals)
    print()
    print(teams_bronze)
    print("bronze medals: ",counter_for_bronze_medals)
    print()
    print(teams_silver)
    print("silver medals: ",counter_for_silver_medals)
