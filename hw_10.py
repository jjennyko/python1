#1.
import pandas as pd
# df.loc[ '2013-01-01', 'A'] 取出 '2013-01-01'列的 'A'欄資料值
# df.loc[ '2013-01-01', ['A', 'B'] ] 取出 '2013-01-01'列的 'A','B'欄資料值
# df.loc[ '2013-01-01':'2013-01-02', 'A' ] 取出 '2013-01-01'到 '2013-01-02'列的 'A'欄資料值
# df.loc[ '2013-01-01':'2013-01-05', 'A':'C'] 取出 '2013-01-01'到'2013-01-05'列的 'A'到'C'欄資料值

#2.
df = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df[0:3])
print(df[df.index%2==1])
print(df.iloc[:,-2:])
print(df.iloc[0::2])

#3.
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df[df[0]>20])
print(df[df[0]+df[1]>50])
print(df[(df[0]<30) | (df[1]>30)])
print(df[df.sum(axis=1)>100])