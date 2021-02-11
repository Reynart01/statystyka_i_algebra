import cx_Oracle
import pandas as pd
from pandas import DataFrame, read_csv

def SaveDataToDb(file, tableName):

  dsn_tns = cx_Oracle.makedsn('213.184.8.44', '1521', service_name='orac') 
  conn = cx_Oracle.connect(user=r'wegrodzki', password='dobrehaslo321', dsn=dsn_tns)
  cursor = conn.cursor()


  dataset = pd.read_csv(file, delimiter=",")

  df_list = dataset.values.tolist()

  sql='insert into wegrodzki.'+tableName+' values('

  for i in range(dataset.shape[1]):
    sql += ':' + str(i + 1) + ','

  sql = sql[:len(sql)-1]
  sql += ')'

  if dataset.date is not None:
    sql = sql.replace(':2', "TO_DATE(:2,'YYYY-MM-DD')")

  n = len(df_list)


  for i in range(n):
      cursor.execute(sql,df_list[i])

  conn.commit()


# SaveDataToDb('products.csv', 'products')
# SaveDataToDb('sellers.csv', 'sellers')
#SaveDataToDb('chleb_razowy_1.csv', 'products_prices')
# SaveDataToDb('chleb_razowy_2.csv', 'products_prices')
# SaveDataToDb('chleb_baltonowski_1.csv', 'products_prices')
# SaveDataToDb('chleb_baltonowski_2.csv', 'products_prices')
# SaveDataToDb('cola_1.csv', 'products_prices')
# SaveDataToDb('cola_2.csv', 'products_prices')
# SaveDataToDb('ryzen_1.csv', 'products_prices')
# SaveDataToDb('ryzen_2.csv', 'products_prices')