import pandas as pd

# Caminhos para a pasta data
c1 = "data/club_league.csv"
c2 = "data/clubs.csv"
c3 = "data/leagues.csv"
c4 = "data/players.csv"
c5 = "data/transfers.csv"

# Leitura dos arquivos usando os caminhos
d1 = pd.read_csv(c1, sep=';')
d2 = pd.read_csv(c2, sep=';')
d3 = pd.read_csv(c3, sep=';')
d4 = pd.read_csv(c4, sep=';')
d5 = pd.read_csv(c5, sep=';')

print(d1.head())
print(d2.head())
print(d3.head())
print(d4.head())
print(d5.head())