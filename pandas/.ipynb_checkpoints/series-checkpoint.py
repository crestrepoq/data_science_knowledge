import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(arr)
print(d)

print('\n')
print('Usando pd.Series:')
print(pd.Series(data = my_data))
print('\r')
print(pd.Series(data = labels))
print('\r')
print(pd.Series(data=my_data,index=labels))
print('\r')
print(pd.Series(my_data,labels))

print('\r')
print('Usando pd.Series y arrays:')
print(pd.Series(arr,labels))

print('\r')
print('Usando pd.Series y diccionarios:')
print(pd.Series(d))

print('\r')
print('Usando pd.Series y listas:')
ser1 = pd.Series([1,2,3,4],['USA','Germany','URSS','Japan'])
print(ser1)

print('\r')
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

print('\r')
print('Buscando por index como si fuera un dict:')
print(ser1['USA'])

print('\r')
print('Sumando dos series por index, si no encuentra relacion, ponen "nan":')
print(ser1 + ser2)
