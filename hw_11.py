#1.
import pandas as pd
import numpy as np
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)
df1=df.sort_values(by=['age'])
df2=df1.sort_values(by=['visits'],ascending=False)
df['priority']=df['priority'].str.replace('yes','True')
df['priority']=df['priority'].str.replace('no','False')
#2.
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
print(df.apply(lambda i : i-i.mean(axis=0)))
print(df.apply(lambda i : i-df.mean(axis=1)))

# 哪一筆的資料總合最小
print(df.sum(axis=0).argmin())
# 哪一欄位的資料總合最小
print(df.sum(axis=1).argmin())