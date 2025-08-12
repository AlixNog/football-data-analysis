import pandas as pd


c1 = "club_league.csv"
c2 = "clubs.csv"
c3 = "leagues.csv"
c4 = "players.csv"
c5 = "transfers.csv"


d1 = pd.read_csv("club_league.csv", sep=';')
d2 = pd.read_csv("clubs.csv", sep=';')
d3 = pd.read_csv("leagues.csv", sep=';')
d4 = pd.read_csv("players.csv", sep=';')
d5 = pd.read_csv("transfers.csv", sep=';')

print(d1.head())
print(d2.head())
print(d3.head())
print(d4.head())
print(d5.head())