import numpy as np

arr = np.arange(0,11)
print(arr)

print('position 8 with [8]:')
print(arr[8])

print('Starting index and stop index:')
print(arr[0:5])
print(arr[1:5])
print(arr[:6])
print(arr[5:])

print('Cambiar los valores de elementos en posiciones particulares con indexing:')
arr[0:5]=100
print(arr)

print('\n')
arr = np.arange(0,11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:] = 99
print('Array con valores cambiados a 99')
print(slice_of_arr)
print('Si hago un cambio en una variable que contenia el array original, este ultimo tambien cambia:')
print(arr)

print('\n')
print('Para evitar sobreescribir los arrays se usa .copy()')
arr_copy = arr.copy()
print(arr)
arr_copy[:] = 100
print(arr_copy)
print(arr)

#Last changes
