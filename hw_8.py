#1.
# 對於資料格式有高度的銜接性，包含 CSV、Excel 或資料庫（SQL）皆能提供彈性的讀寫工具

#2.
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/MachineLearningLiuMing/scikit-learn-primer-guide/master/Data.csv')
print(df)
print(df.shape)
print(df.size)
print(df.values)
print(df.index)
print(df.columns)
print(df.dtypes)
print(len(df))