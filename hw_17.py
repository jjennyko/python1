#1.
import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
print(series) 
#2.
week = series.to_period('W')
print(week) 
#3.
week = series.resample('W', convention='start').mean()
print(week) 