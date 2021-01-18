import pandas as pd
import numpy as np

array = pd.Series(['Apple', 'Banana', 'Carrot'], index=['a', 'b', 'c'])
print(array)
print(array['a'])

word_dict = {
    'Apple': 'New York',
    'Banana': 'Los Angeles',
    'Carrot': 'Tokyo',
    'Durian': 'Milano'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)
print("==============================================")
print(summary.notnull())
print("=============================================")
print(summary.isnull())
print("=============================================")
summary['frequency'] = summary['frequency'].fillna('No Data')
print(summary)
print("=======La Fine=================================")

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)

