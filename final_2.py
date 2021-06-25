import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

from pandas_profiling import ProfileReport
import numpy as np 
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir('/content/drive/My Drive/Colab Notebooks/Python/Netflix')
os.listdir()

df = pd.read_csv("netflix_titles.csv")
#檢視資料的項目
df.head()

df.info()
report = ProfileReport(df)
report.to_notebook_iframe()
df.nunique()
df.isna().sum()
df['rating'].unique()
df['rating'].isna()
df[df['rating'].isna()]
rating_replacements = {
    211: 'TV-14',
    2411: 'TV-14',
    3288: 'PG-13',
    4056: 'TV-G',
    4402: 'TV-G',
    4403: 'TV-G',
    4706: 'TV-14',
    5015: 'TV-14',
    5234: 'TV-14',
    6231: 'TV-Y'
}

for id, rate in rating_replacements.items():
    df.iloc[id, 8] = rate
    
df['rating'].isna().sum()
df = df.drop(['director', 'cast'], axis=1)
df.columns
df[df['date_added'].isna()]
df = df[df['date_added'].notna()]
df['country'] = df['country'].fillna(df['country'].mode()[0])
df.isna().sum()
df.head()
df['year_added'] = df['date_added'].apply(lambda x: x.split(" ")[-1])
df['year_added'].head()
df['month_added'] = df['date_added'].apply(lambda x: x.split(" ")[0])
df['month_added'].head()
