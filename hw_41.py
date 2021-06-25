import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import sklearn
print(sklearn.__version__)
print(pd.__version__)
%matplotlib inline

from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing

from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

print(df_train.info())
df_train['Survived_cate']=df_train['Survived']
df_train['Survived_cate']=df_train['Survived_cate'].astype('object')
print(df_train.info())
complete_data=complete_data.drop(['Name','Ticket','PassengerId'], axis=1)
display(complete_data.head(5))

print(complete_data.shape)
num_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'float64' or dtype == 'int64':
        num_features.append(feature)
print(f'{len(num_features)} Numeric Features : {num_features}\n')
cat_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'object':
        cat_features.append(feature)
print(f'{len(cat_features)} category Features : {cat_features}\n')
x=complete_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked']]
y=complete_data['Survived']
display(x.head(5))
display(y.head(5))
x = x.copy()
c = x.loc[:,'Sex'].astype('category')
d = dict(enumerate(c.cat.categories))
x['Sex'] = x['Sex'].astype('category').cat.codes
c = x['Embarked'].astype('category')
d = dict(enumerate(c.cat.categories))
x['Embarked'] = x['Embarked'].astype('category').cat.codes
x.head()
sex_mapping = {'female': 0, 'male': 1}
x['Sex'] = x['Sex'].map(sex_mapping)
embark_mapping = {'C': 0, 'Q': 1, 'S': 2}
x['Embarked'] = x['Embarked'].map(embark_mapping)
estimator = SVC(kernel="linear")
selector = RFE(estimator, n_features_to_select=1, step=1)
selector = selector.fit(x,y)
print(selector.support_)
ranking = selector.ranking_
print(ranking)
rfe_feature = x.loc[:,selector.support_].columns.tolist()
print(rfe_feature)