import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,180)
y = np.cos(x * np.pi / 180.0)

plt.plot(x,y)
plt.show()
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)

plt.plot(x, y_sin)

plt.show()
x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.title("順便解決中文問題")

plt.plot(x, y_cos)
plt.savefig("D18_資料視覺化.png",dpi=300,format="png")