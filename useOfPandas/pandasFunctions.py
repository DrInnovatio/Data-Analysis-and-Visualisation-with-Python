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
print("==============================================")
print(summary.isnull())
print("==============================================")
summary['frequency'] = summary['frequency'].fillna('No Data')
print(summary)
print("==============================================")

array_1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array_2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])
array = array_1.add(array_2, fill_value=0)
print(array)

print("===================== 2 =======================")

arr_1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
arr_2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

arr = arr_1.add(arr_2, fill_value=0)
print(arr)
print("Sum of column 1 : ", arr[1].sum())
print(arr.sum())

print("===================== 3 =======================")

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)
print(brics)

print("===================== 4 =======================")

dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])
print(dfa)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

colors = pd.Series(
    ["red", "purple", "blue", "green", "yellow"],
    index=[1, 2, 3, 5, 8]
)
print(colors)

arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
          ['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},
                  index=index)
print(df)