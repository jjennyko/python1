from pandas_profiling import ProfileReport
import numpy as np 
import pandas as pd
# 載入繪圖相關套件
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.info())print(df.isnull().sum())
print(df['rating'].unique())
print(df[df['rating'].isnull()])

rating_replace={
    211: 'TV-14',
    2411: 'TV-14',
    3288: 'PG-13',
    4056: 'TV-G',
    4402: 'TV-G',
    4403: 'TV-G',
    4706: 'TV-14',
    5015: 'TV-14',
    5234: 'TV-14',
    6231: 'TV-Y'}
for id,rate in rating_replace.items():
    df.iloc[id,8]=rate
print(df['rating'].isnull().sum())

df = df.drop(['director', 'cast'], axis = 1)
print(df.info())
print(df[df['date_added'].isnull()])
df=df[df['date_added'].notna()]
print(df['date_added'].isnull().sum())
print(df.info())
df['country']=df['country'].fillna(df['country'].mode()[0])
print(df.isnull().sum())
df['years'] = df['date_added'].apply(lambda x : x.split(" ")[-1])
print(df['years'].head())
df['months'] = df['date_added'].apply(lambda x : x.split(" ")[0])
print(df['months'].head())
print(df['rating'].unique())
ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
df['target_ages']=df['rating'].replace(ratings_ages)
print(df['target_ages'].unique())

# Lets retrieve just the first country 取第一個國家
df['country_first']=df['country'].apply(lambda x : x.split(",")[0])
print(df['country_first'].head())
# 修正日期型別
print(df.dtypes)
df['type']=df['type'].astype('category')
df['target_ages']=df['target_ages'].astype('category')
df['years']=df['years'].astype('int64')
print(df.dtypes)

# 資料視覺化
df['genre'] = df['listed_in'].apply(lambda x : x.split(','))
print(df['genre'].head())
print(df['type'].unique())
movie_df = df[df['type']=='Movie']
show_df = df[df['type']=='TV Show']
print(movie_df.head())
print(show_df.head())

# TV shows 跟 Movies的比例
print(df['type'].value_counts().reset_index())
# fig = px.pie(df['type'].value_counts().reset_index(),values = 'type', names = 'index')
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

#新增rating 的資料子集
#方便做年齡層的分布查詢
def generate_rating_df(df):
    rating_df = df.groupby(['rating', 'target_ages']).agg({'show_id': 'count'}).reset_index()
    rating_df = rating_df[rating_df['show_id'] != 0]
    rating_df.columns = ['rating', 'target_ages', 'counts']
    rating_df = rating_df.sort_values('target_ages',ascending=True).reset_index(drop = True)
    return rating_df
rating_df = generate_rating_df(df)
print(rating_df)
# fig = px.bar(rating_df, x='rating', y='counts', color='target_ages')
# fig.show()

# 針對影集或是歌劇
movie_df1 = generate_rating_df(movie_df)
print(movie_df1)
show_df1 = generate_rating_df(show_df)
print(show_df1)


# 按國別分別顯示影集與歌劇的產出分布,使用圓餅圖
country_df = df['country_first'].value_counts().reset_index()
print(country_df)
country_df = country_df[country_df['country_first']/country_df['country_first'].sum()>0.01]
print(country_df)
# fig = px.pie(country_df, values='country_first', names='index')
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

# 按國別分別顯示影集與歌劇的產出分布,使用歷史分布
# fig = px.histogram(df,x='country_first')
# fig.update_xaxes(categoryorder='total descending') #最多到最少
# fig.show()

# 發佈內容
# 我們可以看到，在過去的幾年中，內容製作的數量在增加
release_year_df = df.loc[df['release_year'] > 2010].groupby(['release_year', 'type']).agg({'show_id':'count'}).reset_index()
add_year_df = df.loc[df['years'] > 2010].groupby(['years', 'type']).agg({'show_id':'count'}).reset_index()
print(release_year_df)
print(add_year_df)
from scipy.stats import norm
import matplotlib
matplotlib.use('TKAgg')
# sns.distplot(df.loc[df['release_year'] > 2000, 'release_year'], fit=norm, kde=False)
# plt.show()
#displot()集合了matplotlib的hist()與核函數估計kdeplot的功能，
#增加了rugplot分佈觀測條顯示與利用scipy庫fit擬合參數分佈的新穎用途。
#fit：控制擬合的參數分佈圖形，能夠直觀地評估它與觀察數據的對應關係(黑色線條為確定的分佈)

#導入SKLEARN的前處理套件, 將元素進行二元變換 , 輸入的資料會轉換成一個 一維 classes_
#每組資料會轉換成和 classes_ 相同大小的一維陣列
#如果資料有對應到 classes_  就為 1 否則為 0
from sklearn.preprocessing import MultiLabelBinarizer
def calculate_mlb(series):
    mlb = MultiLabelBinarizer()
    mlb_df = pd.DataFrame(mlb.fit_transform(series), columns=mlb.classes_, index=series.index)
    return mlb_df
print(calculate_mlb(df['genre']))

#如何在csv文件中將一列拆分為單獨的列
def top_genres(df, title='Top ones'):
    genres_df = calculate_mlb(df['genre'])
    tdata = genres_df.sum().sort_values(ascending=False)
    return tdata 
print(top_genres(df))
# fig = go.Figure(go.Bar(x=top_genres(df).index, y=top_genres(df).values))
# fig.update_xaxes(categoryorder='total descending')
# fig.update_layout(title='Top ones')
# fig.show()

print(top_genres(movie_df, title='Top Movies Genres'))
print(top_genres(show_df, title='Top TV-Shows Genres'))

#如何在csv文件中將一列拆分為單獨的列
genres_df = calculate_mlb(movie_df['genre'])
movie_corr = genres_df.corr()
print(movie_corr)
movie_mask = np.zeros_like(movie_corr,dtype = np.bool)
print(movie_mask)
movie_mask[np.triu_indices_from(movie_mask)] = True
# fig, ax = plt.subplots(figsize=(10,7))
# pl = sns.heatmap(movie_corr, mask=movie_mask, cmap='coolwarm',vmax=0.5, vmin=-0.5, center=0, linewidths=0.5,
#                  cbar_kws={'shrink':0.6})
# plt.show()

genres_df = calculate_mlb(show_df['genre'])
show_corr = genres_df.corr()
show_mask = np.zeros_like(show_corr, dtype=np.bool)
show_mask[np.triu_indices_from(show_mask)] = True
fig, ax = plt.subplots(figsize=(10, 7))
pl = sns.heatmap(show_corr, mask=show_mask, cmap= "coolwarm", vmax=.5, vmin=-.5, center=0, linewidths=.5,
                 cbar_kws={"shrink": 0.6})
plt.show()

# 使用文字雲, 找出最多被使用在資料集上的描述
# 對文本數據中出現頻率較高的“關鍵詞”在視覺上的突出呈現，
# 形成關鍵詞的渲染形成類似雲一樣的彩色圖片，從而一眼就可以領略文本數據的主要表達意思
from wordcloud import WordCloud