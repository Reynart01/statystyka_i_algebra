from datetime import datetime, date
from datetime import timedelta  
import random
import csv
import pandas as pd

class ProductPrice:
  def __init__(self, date, price, productId, sellerId):
    self.date = date
    self.price = price
    self.productId = productId
    self.sellerId = sellerId

  def printObject(self):
    print('Date: {0}\nPrice: {1}\nProductId: {2}'.format(self.date, self.price, self.productId))


def GenerateData(prices, firstDay, lastDay, productId, sellerId):
  
  random.shuffle(prices)

  numberOfPrices = len(prices)

  days = (lastDay - firstDay).days

  changes = []
  for i in range(numberOfPrices - 1):
    changes.append( random.randrange(days + 1))
  
  changes.append(days)

  changes.sort()

  result = []
  
  print(changes)
  currentDate = firstDay

  for i in  range(len(changes)):    
    nextChangeDate = firstDay + timedelta(days = changes[i])
    while currentDate != nextChangeDate:
      result.append(ProductPrice(currentDate, prices[i], productId, sellerId)) 
      currentDate = currentDate + timedelta(days=1)
  
  return result

def SaveToFile(filename, objects, previousItemId):
  with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['no.', 'date', 'price', 'productId', 'sellerId'])
    for i in range(len(objects)):
      writer.writerow([previousItemId + i + 1, objects[i].date, objects[i].price, objects[i].productId, objects[i].sellerId])


#chleb = GenerateData([2.8, 3, 3.4, 3.8, 4.1], date(2019, 2,1), date(2021, 2,1), productId = 1, sellerId = 2)
#SaveToFile('chleb_razowy_2.csv', chleb, 731)

#chleb = GenerateData([1.9, 2.2, 2.5, 2.8, 3.4], date(2019, 2,1), date(2021, 2,1), productId = 2, sellerId = 1)
#SaveToFile('chleb_baltonowski_1.csv', chleb, 1462)

#chleb = GenerateData([2, 2.1, 2.3, 2.4, 2.9, 3.6], date(2019, 2,1), date(2021, 2,1), productId = 2, sellerId = 2)
#SaveToFile('chleb_baltonowski_2.csv', chleb, 2193)

#cola = GenerateData([4.5, 4.9, 5, 5.5, 6, 7], date(2019, 2,1), date(2021, 2,1), productId = 3, sellerId = 3)
#SaveToFile('cola_1.csv', cola, 2924)

# cola = GenerateData([5, 4.9, 5.2, 5.5, 6, 8], date(2019, 2,1), date(2021, 2,1), productId = 3, sellerId = 4)
# SaveToFile('cola_2.csv', cola, 3655)


# ryzen = GenerateData([792, 859, 883, 929, 899, 939, 855, 829], date(2019, 2,1), date(2021, 2,1), productId = 4, sellerId = 5)
# SaveToFile('ryzen_1.csv', ryzen, 4386)

# ryzen = GenerateData([792, 859, 883, 929, 899, 939, 855, 829], date(2019, 2,1), date(2021, 2,1), productId = 4, sellerId = 6)
# SaveToFile('ryzen_2.csv', ryzen, 5117)










