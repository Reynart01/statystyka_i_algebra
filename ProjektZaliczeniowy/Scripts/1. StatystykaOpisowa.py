import numpy as np
import cx_Oracle


class ProductPrice:
  def __init__(self, date, price, product, seller):
    self.date = date
    self.price = price
    self.product = product
    self.seller = seller

  def printObject(self):
    print('Date: {0} Price: {1} Product: {2} Seller: {3}'.format(self.date, self.price, self.product, self.seller))


def PrintStatisticts(productName, startDate, endDate):

  dsn_tns = cx_Oracle.makedsn('213.184.8.44', '1521', service_name='orac') 
  conn = cx_Oracle.connect(user=r'wegrodzki', password='dobrehaslo321', dsn=dsn_tns)

  sqlCommand = open("Scripts/GetProductPricesByNameAndMonth.sql", "r").read()

  
  cursor = conn.cursor()

  cursor.execute(sqlCommand, {'name': productName, 'startDate': startDate, 'endDate': endDate})

  productPrices = []
  for row in cursor:
      productPrices.append(ProductPrice(row[0], row[1], row[2], row[3]))
  conn.close()

  prices = [p.price for p in productPrices]

  print(productName + ' ' + startDate + ' - ' + endDate +  '\n-----------------------')

  print('mean price: ' + str(round(np.mean(prices),2)))
  print('median price: ' + str(round(np.median(prices),2)))
  print('max price: ' + str(round(np.max(prices),2)))
  print('min price: ' + str(round(np.min(prices),2)))
  print('standard deviation of price: ' + str(round(np.std(prices),2)))
  print('variance of price: ' + str(round(np.var(prices),2)))
  print('')


PrintStatisticts('chleb razowy', '2019-02-01', '2021-01-31')

PrintStatisticts('chleb baltonowski', '2019-02-01', '2021-01-31')

PrintStatisticts('coca cola 1.5l', '2019-02-01', '2021-01-31')

PrintStatisticts('AMD Ryzen 5 3600', '2019-02-01', '2021-01-31')


PrintStatisticts('chleb razowy', '2020-02-01', '2020-05-31')

PrintStatisticts('chleb baltonowski', '2020-02-01', '2020-05-31')

PrintStatisticts('coca cola 1.5l',  '2020-02-01', '2020-05-31')

PrintStatisticts('AMD Ryzen 5 3600',  '2020-02-01', '2020-05-31')