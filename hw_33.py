import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
import statsmodels.stats.proportion

#H1=生產線A=/生產線B
#H0=生產線A=生產線B

A = [75,30] # 有開信的個數
B = [300,300] #各組實驗總個數
statsmodels.stats.proportion.proportions_ztest(A, B, alternative='smaller')

#Answer: >0.05, 沒有不同