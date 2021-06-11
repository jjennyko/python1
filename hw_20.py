import matplotlib.pyplot as plt

#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度, 若不給定值, 圖的周邊無文字
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)


#第二層
plt.axes([.18, .18, .5, .5])
plt.xticks([]), plt.yticks([])
plt.text(0.1, 0.1, 'axes([.18, .18, .5, .5])', ha='left', va='center', size=16, alpha=.5)

#第三層
plt.axes([.26, .26, .5, .5])
plt.xticks([]), plt.yticks()
plt.text(0.1, 0.1, 'axes([.26, .26, .5, .5])', ha='left', va='center', size=16, alpha=.5)

#第四層
plt.axes([.34, .34, .5, .5])
plt.xticks([]), plt.yticks()
plt.text(0.1, 0.1, 'axes([.34, .34, .5, .5])', ha='left', va='center', size=16, alpha=.5)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

 #配置12 組 Bar
n = 12 
X = np.arange(n)

 #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# +Y 指的是 XY 四象限的第一象限
# -Y 指的是 XY 四象限的第二象限

plt.bar(X, -Y1, facecolor='r', edgecolor='w')

#設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x, y, '%.2f' % y, ha='center', va= 'bottom')

#設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()

