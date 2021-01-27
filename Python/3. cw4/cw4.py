import scipy.stats as scs
import statistics as stat
import pandas as pd

#zad 1
print('zad 1')

data = scs.norm.rvs(loc=2, scale=30, size=200)

test = scs.ttest_1samp(data, 2.5)

print(test)


#zad 2
print('\n\nzad 2')

napoje = pd.read_csv('3. cw4\\napoje.csv', delimiter=';')

testLech = scs.ttest_1samp(napoje.lech, 60500)
print('Lech: ')
print(napoje.lech.mean())
print( testLech)

tetCola = scs.ttest_1samp(napoje.cola, 222000)
print('Cola: ')
print(napoje.cola.mean())
print( tetCola)

testRegionalne = scs.ttest_1samp(napoje.regionalne, 43500)
print('Regionalne: ')
print(napoje.regionalne.mean())
print(testRegionalne)

#zad 3
print('\n\nzad 3')

print('Test normalnosci dla pepsi:')
print(scs.normaltest(napoje.pepsi))

print('Test normalnosci dla fanty:')
print(scs.normaltest(napoje.fanta))

print('Test normalnosci dla żywca:')
print(scs.normaltest(napoje.zywiec))

print('Test normalnosci dla okocim:')
print(scs.normaltest(napoje.okocim))

print('Test normalnosci dla regionalnego:')
print(scs.normaltest(napoje.regionalne))

print('Test normalnosci dla coli:')
print(scs.normaltest(napoje.cola))

print('Test normalnosci dla lecha:')
print(scs.normaltest(napoje.lech))

print('Przy założeniu że dla p>0.05 nie podstaw do odrzucenia hipotezy')
print('Zmienna regionalne nie wykazuje normalności, pozostałe wykazują.')