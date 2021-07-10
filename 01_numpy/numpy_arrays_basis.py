import numpy as np

my_list = [1,2,3]

print('Crear un array con una lista:')
arr = np.array(my_list)
print(arr)

print('Crear un array de dos dimensiones con una lista de listas:')
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

#np.arange es la forma mas comun para crear un array en python
#El tercer valor valida si es un numero par o impar
print('Crear un array con un rango:')
print(np.arange(0,10,2))

print('Crear arrays con 0s:')
print(np.zeros(3))
print(np.zeros((2,3)))

print('Crear arrays con 1s:')
print(np.ones((3,4)))

print('Array con distancia definida usando linspace')
#El 3er valor es la cantidad de puntos que se quieren
print(np.linspace(0,5,100))

#crear una matriz de identidad con np.eye()
print('Matriz de identidad en dos dimensiones')
print(np.eye(4))

#Devolver un array con valores con distribucion uniforme
print('Array con valores con distribucion uniforme:')
print('Array de una dimension:')
print(np.random.rand(5))
print('Array de dos dimensiones:')
print(np.random.rand(5,5))

#Devolver una muestra con una distribucion normal usar np.random.randn()
print('Devolver valores aleatorios de la distribucion normal')
print('Valores aleatorios para un array de una dimension con distribucion normal:')
print(np.random.randn(2))
print('Valores aleatorios para un array de dos dimensiones con distribucion normal:')
print(np.random.randn(4,4))

#Randint - devuelve numeros enteros aleatorios
print('Array con un número entero aleatorios entre dos valores:')
print(np.random.randint(1,100))
print('Array con numeros enteros aleatorios:')
print(np.random.randint(1,100,10))

#Last changes
