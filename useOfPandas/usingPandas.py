import pandas as pd

array = pd.Series(['Apple', 'Banana', 'Carrot'], index=['a', 'b', 'c'])
print(array)
print(array['a'])

word_dict = {
    'Apple': 'New York',
    'Grape': 'Paris',
    'Banana': 'Los Angeles'
}

frequency_dict = {
    'Apple': 3,
    'Grape': 5,
    'Banana': 7
}

importance_dict = {
    'Apple': 3,
    'Grape': 2,
    'Banana': 1
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

# score = summary['frequency'] * summary['importance']
# summary['score'] = score

summary.loc['Apple', 'importance'] = 5
summary.loc['Elderberry'] = ['Elder', 5, 3]


