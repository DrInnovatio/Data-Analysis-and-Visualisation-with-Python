# [1,2,3,4] * 2 (scala) = [2,4,6,8]

import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
result_array = array * 10
print(result_array)