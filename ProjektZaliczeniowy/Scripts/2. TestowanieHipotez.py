import scipy.stats as scs
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


def PrintNormaltestsResults(productName, startDate, endDate):

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

  print('normal test: ' + str(scs.normaltest(prices))+'\n\n')



def PrintTestResults(productName, startDate, endDate, testValue):

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

  print(str(scs.ttest_1samp(prices, testValue))+'\n\n')


  

PrintNormaltestsResults('chleb razowy', '2019-02-01', '2021-01-31')

PrintNormaltestsResults('chleb baltonowski', '2019-02-01', '2021-01-31')

PrintNormaltestsResults('coca cola 1.5l', '2019-02-01', '2021-01-31')

PrintNormaltestsResults('AMD Ryzen 5 3600', '2019-02-01', '2021-01-31')


PrintNormaltestsResults('chleb razowy', '2020-02-01', '2020-05-31')

PrintNormaltestsResults('chleb baltonowski', '2020-02-01', '2020-05-31')

PrintNormaltestsResults('coca cola 1.5l',  '2020-02-01', '2020-05-31')

PrintNormaltestsResults('AMD Ryzen 5 3600',  '2020-02-01', '2020-05-31')

PrintTestResults('chleb razowy', '2019-02-01', '2021-01-31', testValue=3.5)

PrintTestResults('chleb razowy', '2020-02-01', '2020-05-31', testValue=3.5)