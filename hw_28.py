import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
#二項次分配
n=100
p=0.5
x=50
probs = stats.binom.pmf(x,n,p)
print('出現正面50次機率=',probs)