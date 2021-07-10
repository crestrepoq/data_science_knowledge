import numpy as np

arr_2d = np.array([[5,10,15],[20,25,30],[30,40,45]])
print(arr_2d)

print('get number 25 with indexing:')
print(arr_2d[1][1])
print('get number 40 with indexing and comma (","):')
print(arr_2d[2,1])
print('using slicing for getting specific values of each column:')
print(arr_2d[:2,1:])
print(arr_2d[:2])

print('\n')
print('Filtering with arrays:')

arr = np.arange(1,11)
print(arr)
bool_arr = arr > 5
print(bool_arr)
print('get values with bolean verification equal to True:')
print(arr[bool_arr])
print(arr[arr>5])
print(arr[arr<3])

print('\n')

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3])
print(arr_2d[1:3,3:5])

#Last changes
