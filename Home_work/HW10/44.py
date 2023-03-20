import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# print(data.head())

#### решение через get_dummies
new_data = pd.get_dummies(data['whoAmI'])
print(new_data.head())

#### решение без get_dummies
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data.loc[data['whoAmI'] != 'robot', 'robot'] = 0
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.loc[data['whoAmI'] != 'human', 'human'] = 0
new_data = data[['human', 'robot']]
print(new_data.head())