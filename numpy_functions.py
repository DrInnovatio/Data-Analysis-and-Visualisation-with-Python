# [1,2,3,4] * 2 (scala) = [2,4,6,8]

import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
result_array = array * 10
print(result_array)

""" The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. 
Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible 
shapes. Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python. 
It does this without making needless copies of data and usually leads to   efficient algorithm implementations. There 
are, however, cases where broadcasting is a bad idea because it leads to inefficient use of     memory that slows 
computation. """

array_1 = np.arange(4).reshape(2, 2)
array_2 = np.arange(2)
array_3 = array_1 + array_2
print(array_3)

# Numpy can calculate different shapes of arrays.

array_4 = np.arange(0, 8).reshape(2, 4)
array_5 = np.arange(0, 8).reshape(2, 4)
array_6 = np.concatenate([array_4, array_5], axis=0)
array_7 = np.arange(0, 4).reshape(4, 1)
print(array_6 + array_7)

# Masking

arr_1 = np.arange(16).reshape(4, 4)
print(arr_1)

arr_2 = arr_1 < 10
print(arr_2)

arr_1[arr_2] = 100
print(arr_1)

# Calculations of Numpy

arr_3 = np.arange(16).reshape(4, 4)
print("Max_value : ", np.max(arr_3))
print("Min_value : ", np.min(arr_3))
print("Total : ", np.sum(arr_3))
print("Average : ", np.mean(arr_3))
print(arr_3)
print("Total of each column : ", np.sum(arr_3, axis=0))