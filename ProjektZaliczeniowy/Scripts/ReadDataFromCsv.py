import pandas as pd

data = pd.read_csv('chleb_razowy.csv', sep=',')


for index, row in data.iterrows():
  print(row['price'])

