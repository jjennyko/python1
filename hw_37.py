import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display

df_train = pd.read_csv("Titanic_train.csv")
df_train.head(5)

g = sns.catplot(x="Sex", y="Age", hue="Sex",
               data=df_train, kind="box")
g = sns.catplot(x="Sex", y="Pclass", hue="Sex",
               data=df_train, kind="box")
data = df_train.copy()

from sklearn import preprocessing
le= preprocessing.LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
data = data[['Age','Pclass','Sex']]
display(data[data.isnull().values==True].head(5))
missing = data.isnull()
print(missing.sum())
value_neighbors = 1
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=value_neighbors,weights='uniform')
data_filled = pd.DataFrame(imputer.fit_transform(data),columns=['Age','Pclass','Sex'])
display(data_filled[missing.values==True].head(5))
missing_count = data_filled['Age'].isnull().sum()
print(f'missing count = {missing_count}')