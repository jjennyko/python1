import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,
 164, 173, 165, 163, 177, 171]
girls=[169, 183, 170, 168, 182, 170, 173, 185, 151, 156, 162, 169, 162, 181,
 159, 154, 167, 175, 170, 160]

#1.
#平均數
print("男生平均=",statistics.mean(boys))
print("女生平均=",np.mean(girls))
#中位數
print("男生中位數=",statistics.median(boys))
print("女生中位數=",np.median(girls))
#標準差
print("男生標準差=",statistics.stdev(boys))
print("女生標準差=",np.std(girls,ddof=1))
#眾數
print("男生眾數=",statistics.mode(boys))
print("女生眾數=",stats.mode(girls,axis=None))
print("女生眾數=",stats.mode(girls,axis=None)[0][0])
#變異數
print("男生身高變異數=",statistics.variance(boys))
print("女生身高變異數=",np.var(boys,ddof=1))
#百分位數
print("男生20百分位數=",stats.scoreatpercentile(boys, 20))
print("女生20百分位數=",np.percentile(girls, 20))
#偏度
print("男生偏度=",stats.skew(boys))
print("女生偏度=",stats.skew(girls))
#峰度
print("男生峰度=",stats.kurtosis(boys))
print("女生峰度=",stats.kurtosis(girls))

#2.
print("男生平均身高=",np.mean(boys))
print("女生平均身高=",np.mean(girls))
if np.mean(boys)>np.mean(girls):
    print("男生平均身高比較高")
else :
    print("女生身高比較高")
#3.
print("Q3答案:不一致,因為樣品數太少,可能抽到離值群較大的數")