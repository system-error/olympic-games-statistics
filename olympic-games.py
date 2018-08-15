import csv

with open('athlete_events.csv',mode='r') as csvfile:
     olympic_games_file = csv.reader(csvfile)
     for row in olympic_games_file:
         print(', '.join(row))