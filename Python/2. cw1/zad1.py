import pandas as pd
import numpy as np
import statistics
from scipy import mean
import matplotlib.pyplot as plt

print('zadanie 1\n')
data1 = pd.read_csv('2. cw1\\MDR_RR_TB_burden_estimates_2020-10-29.csv')

col = data1['e_rr_pct_new_lo']

print('mean: ' + str(col.mean()))
print('median: ' + str(col.median()))
print('max: ' + str(col.max()))
print('min: ' + str(col.min()))
print('standard deviation: ' + str(col.std()))

print('\n\nzadanie 2\n')
data2 = np.loadtxt('2. cw1\\Wzrost.csv', delimiter=',')

print('pstdev(): ' + str(statistics.pstdev(data2)))
print('stdev(): ' + str(statistics.stdev(data2)))
print('pvariance(): ' + str(statistics.pvariance(data2)))
print('variance(): ' + str(statistics.variance(data2)))

#stdev is used when the data is just a sample of the entire population. 
#pstdev is used when the data represents the entire population.

#Same for pvariance and variance

print('\n\nZadanie 4\n')
data4 = pd.read_csv('2. cw1\\brain_size.csv', sep=';')

print('VIQ mean: '+ str( data4['VIQ'].mean()))

print(data4['Gender'].value_counts())

data4['VIQ'].hist()
plt.show()

data4['PIQ'].hist()
plt.show()

data4['FSIQ'].hist()
plt.show()

data4[data4['Gender'] == 'Female']['VIQ'].hist()
plt.show()

data4[data4['Gender'] == 'Female']['PIQ'].hist()
plt.show()

data4[data4['Gender'] == 'Female']['FSIQ'].hist()
plt.show()