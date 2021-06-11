import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.getcwd()

df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")
df_red["color"] = "R"
df_white["color"] = "W"
df_all=pd.concat([df_red,df_white],axis=0)
df_all.head()
df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
df_all.head()
sns.histplot(df_all["quality"])
df = pd.get_dummies(df_all, columns=["color"])
df_all.isnull().sum()
df_all.info()
df_all.describe()
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    

plt.tight_layout(rect=(0, 0, 1.2, 1.2))
x=18
df_all.hist(bins=x, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True)    

plt.tight_layout(rect=(0, 0, 1.2, 1.2))
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)
plt.tight_layout(rect=(0, 0.5, 2, 2))