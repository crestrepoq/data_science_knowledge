import numpy as np

arr = np.arange(0,11)
print(arr)

print('add elements of arrays:')
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr + 100)
print(arr * 100)
print(arr - 100)
print(arr / arr)
print(1 / arr)
print(arr ** 2)

print('\n')
print('Universal array functions:')

print(np.sqrt(arr))
print(np.exp(arr))
print(np.max(arr))
print(arr.max())
print(np.sin(arr))
print(np.log(arr))

#https://numpy.org/doc/stable/reference/ufuncs.html
#Last changes
