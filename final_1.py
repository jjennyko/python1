
import numpy as np 
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
pd.set_option('display.max_rows', None)
from plotly.subplots import make_subplots
data = pd.read_csv("covid_19_data.csv")
print(data.head(20))
print(data.info())
data1 = data.drop_duplicates(subset = None, keep = "first", inplace = False)
if data1.shape[1] == data.shape[1]:
    print("沒有重複")

print(data.isnull().sum())

def Missing_Counts(Data) : 
    missing = Data.isnull().sum()      
    missing.sort_values( ascending=False, inplace=True )  
    Missing_Count = pd.DataFrame( { 'Column Name':missing.index, 'Missing Count':missing.values } ) 
    Missing_Count[ 'Percentage(%)' ] = Missing_Count['Missing Count'].apply( lambda x: '{:.2%}'.format(x/Data.shape[0]))
    return  Missing_Count
print(Missing_Counts(data))
data['Province/State'] = data['Province/State'].fillna('Unknown')
print(data.head(40))
print(data.loc[data['Province/State']=='Unknown'].head(10))
data[['Confirmed','Deaths','Recovered']]=data[['Confirmed','Deaths','Recovered']].astype(int)
print(data.head())
data['Country/Region']=data['Country/Region'].replace('Mainland China','China')
print(data.head())
data['Active_case']=data['Confirmed']-data['Deaths']-data['Recovered']
print(data.info())
Data = data[data['ObservationDate']==max(data['ObservationDate'])].reset_index()
print(Data.head(10))
print(Data.shape[0])
Data_world = Data[['Confirmed','Deaths','Recovered','Active_case']].groupby(Data['ObservationDate']).sum().reset_index()
print(Data_world)
labels=['Last Update','Confirmed','Deaths','Recovered','Active_case']

labels = ['Active cases','Recovered','Deaths']

values = Data_world.loc[0, ['Active_case','Recovered','Deaths']]

data_overtime = data[['Confirmed','Deaths','Recovered','Active_case']].groupby(data['ObservationDate']).sum().reset_index().sort_values('ObservationDate',ascending=True).reset_index(drop=True)
print(data_overtime.head(5))

data_country = Data[['Confirmed','Deaths','Recovered','Active_case']].groupby(Data['Country/Region']).sum().reset_index().sort_values('Confirmed',ascending=False).reset_index(drop=True)
print(data_country.head())
headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

data_country1 = data.groupby(['Country/Region','ObservationDate'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index().sort_values("ObservationDate",ascending=True).reset_index(drop=True)
print(data_country1.head())

Data_Recovered = Data.groupby(['Country/Region'])['Recovered'].sum().reset_index().sort_values("Recovered",ascending=False).reset_index(drop=True)
print(Data_Recovered.head())

Data_Active = Data.groupby(['Country/Region'])['Active_case'].sum().reset_index().sort_values("Active_case",ascending=False).reset_index(drop=True)
print(Data_Active.head())




data_china = data[data['Country/Region']=='China'].reset_index(drop=True)
print(data_china.head())
data_china_last = data_china[data_china['ObservationDate']==max(data_china['ObservationDate'])]
print(data_china_last.head())


data_state = data_china_last.groupby(['Province/State'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index().sort_values('Confirmed',ascending=False).reset_index(drop=True)
print(data_state) 

data_china_total = data_china_last.groupby(['Country/Region'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index(drop=True)
print(data_china_total)


data_china_time = data_china.groupby(['ObservationDate','Country/Region'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index().reset_index(drop=True)
print(data_china_time.head())


data_us = data[data['Country/Region']=='US'].reset_index(drop=True)
print(data_us.head())
data_us_last = data_us[data_us['ObservationDate']==max(data_us['ObservationDate'])].reset_index(drop=True)
print(data_us_last)
data_us_total = data_us_last.groupby(['Country/Region'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index()
print(data_us_total)
labels = ['Deaths','Recovered','Active_case']
values = data_us_total.loc[0,['Deaths','Recovered','Active_case']]

data_us_state = data_us_last.groupby(['Province/State'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index().sort_values('Confirmed',ascending=False).reset_index(drop=True)
print(data_us_state)
data_us_state.drop(57,inplace=True)
print(data_us_state)

data_us_time = data_us.groupby(['ObservationDate','Country/Region'])[['Confirmed','Deaths','Recovered','Active_case']].sum().reset_index().reset_index(drop=True)
print(data_us_time.head())
