#1.
import numpy as np
print(np.zeros((2, 3)))#建立元素全為 0、 1 的陣列
print(np.empty((2, 3)))#元素值則會隨機給定
#2.
a =np.random.rand(2,3)
a=a*100
print(a)
b= a.round()
print(b)
#3.
m=20
n=40
a = np.random.randint(m,n,size=(2,3))
print(a)
b = m+(n-m-1)*np.random.rand(2,3)
print(b.round())
