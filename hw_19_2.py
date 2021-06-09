import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Read = pd.read_csv('boston.csv')
print(Read)
Read_box = pd.DataFrame(Read)
Read.boxplot(figsize=(12,6))
Read_sc = pd.DataFrame(Read)
Read_sc.plot.scatter(x='NOX', y='DIS') 
