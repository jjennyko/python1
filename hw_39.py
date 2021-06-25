import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn  as sns
from scipy import stats
import math
import statistics
%matplotlib inline

df_train = pd.read_csv("Titanic_train.csv")
print(df_train['Fare'].describe())
#觀察: 票價0不合理
print(df_train['Fare'].describe())
Count = len(df_train['Fare'][df_train['Fare'] == 0])
print(f'0 fare count = {Count}')
def outliers_z_score(ys,times):
    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [(y - mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > times)

out_index=outliers_z_score(df_train['Fare'],3)
print(out_index[0])
print("可疑的異常值")
print(df_train.loc[out_index[0],'Fare'])
def outliers_iqr(ys,times):
    quartile_1, quartile_3 = np.nanpercentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * times)
    upper_bound = quartile_3 + (iqr * times)
    return np.where((ys > upper_bound) | (ys < lower_bound))
out_index2=outliers_iqr(df_train['Fare'],1.5)
print(out_index2)
print("用第三種方法的找出的 outlier 有哪些?(1.5 倍IQR)")
print(df_train.loc[out_index2[0],'Fare'])

#觀察: 不是真異常, 不用處理. 因為票價會因不同時間、艙等、購買平台和、床位而有所差異.
