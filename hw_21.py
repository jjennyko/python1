import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")
tips.head()
sns.set(style="darkgrid")
sns.relplot(x="total_bill", y="tip", hue="sex", style="time", data=tips)
fmri.head()
sns.set(style="darkgrid")
sns.relplot(x="timepoint", y="signal", hue="event", style="region", data=fmri)
sns.regplot(x="timepoint", y="signal", data=fmri)