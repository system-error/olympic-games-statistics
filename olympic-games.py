import csv

olympic_games_file = open('../athlete_events.csv','r')

for events in olympic_games_file:
    print(events)