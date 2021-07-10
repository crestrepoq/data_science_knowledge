import numpy as np

arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

print('reshape para cambiar las dimensiones del array:')
print(arr.reshape(5,5))

print('Obtener el maximo elemento del array con max:')
print(ranarr.max())
print('Obtener el minimo elemento del array con min:')
print(ranarr.min())
print('Obtener el index location donde esta el maximo valor con argmax:')
print(ranarr.argmax())
print('Obtener el index location donde esta el minimo valor con argmin:')
print(ranarr.argmin())
print('Obtener la forma o tamanio del vector con shape:')
print(arr.shape)

print('reshape:')
arr = arr.reshape(5,5)
print(arr.shape)

print('Conocer el datatype del array con dtype:')
print(arr.dtype)

#Con este import se puede hacer el llamado directo a la funcion
from numpy.random import randint
print(randint(2,10))

#Last changes

