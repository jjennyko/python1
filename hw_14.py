import pandas as pd

pdb = pd.read_csv("boston.csv",usecols=['CHAS','NOX','RM'])
print(pdb)
pdb.to_excel('my boston.xlsx',sheet_name = 'Boston')

#1.  
df1 = pd.read_csv('https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv')
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--']
)
print(df1)
print(df2)


#2. 
import requests
r = requests.get('https://www.dcard.tw/_api/forums')
response = r.text

import json
data = json.loads(response)
df = pd.DataFrame(data)
df= df.sort_values(by='subscriptionCount', ascending=False)
print(df)
df.to_csv('decard.csv')