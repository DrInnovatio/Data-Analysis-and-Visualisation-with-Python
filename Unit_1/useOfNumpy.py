import numpy as np

''' array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result) '''

'''
array_1 = np.arange(0, 10)
array_2 = np.arange(10, 20)
np.savez('saved.npz', array_1=array_1, array_2=array_2)

data = np.load('saved.npz')
result_1 = data['array_1']
result_2 = data['array_2']
print(result_1)
print(result_2)
'''

'''
# ascending sort
array_3 = np.array([5, 9, 10, 3, 11, 21])
array_3.sort()
print(array_3)

# Descending Sort
print(array_3[::-1])
'''


array_4 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array_4)
array_4.sort(axis=0)
print(array_4)
