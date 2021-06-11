import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('titanic')
df.info()

ax = sns.barplot(x="sex", y="survived", hue="class", data=df)

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
df = sns.load_dataset('tips')
# 利用df.info 檢查有哪些特徵值
df.info()

sns.boxplot(x="day", y="size", data=df)
sns.stripplot(x="day", y="size", data=df, jitter=True)