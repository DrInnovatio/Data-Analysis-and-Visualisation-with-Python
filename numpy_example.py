import numpy as np

# list_data = [1, 2, 3, 4]
# array = np.array(list_data)
#
# print(array.size)
# print(array.dtype)
# print(array[2])

array_1 = np.arange(5)
print(array_1)

array_2 = np.zeros((4, 4), dtype=float)
print(array_2)

array_3 = np.ones((3, 3), dtype=str)
print(array_3)

# 0 to 9 random array
array_4 = np.random.randint(0, 10, (3, 3))
print(array_4)

array_5 = np.random.normal(0, 1, (3, 3))
print(array_5)

# Concatenate()
array_6 = np.randint(0, 10, (1, 1))
array_7 = np.randint(10, 20, (1, 1))
array_8 = np.concatenate([array_6, array_7])
print(array_8.shape)
print(array_8)

array_9 = np.array([1, 2, 3, 4, 5, 6])
array_10 = array_9.reshape((2, 2))
print(array_10)

# 11:13



# The second test
# The second test
# The second test
# The second test
# The second test
# The second test
