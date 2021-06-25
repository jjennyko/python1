import matplotlib.pyplot as plt
from scipy.stats import nbinom
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics

#1.
print('超幾何分配')
#2.
lotto = stats.hypergeom.pmf(6,49,6,6)
print(lotto)
#3.
print('一樣高')
r = np.arange(0,7)
probs = stats.hypergeom.pmf(r,49,6,6)
print(probs)
plt.bar(r,probs)
plt.show()
cumsum_probs = stats.hypergeom.cdf(r,49,6,6)
print(cumsum_probs)
plt.plot(r,cumsum_probs)
plt.show()
x = stats.hypergeom.ppf(cumsum_probs,49,6,6)
print(x)

s = stats.hypergeom.rvs(49,6,6,size=20)
print(s)
plt.hist(s)
plt.show()

stat_hypergeom = stats.hypergeom.stats(49,6,6,moments='mvks')
print(stat_hypergeom)