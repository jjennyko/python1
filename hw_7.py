#1.
import numpy as np 

array1 = np.array([[10, 8], [3, 5]])
array1_inv = np.linalg.inv(array1)
np.dot(array1_inv,array1)
#2.
w, v = np.linalg.eig(array1)
print("特徵值",w)
print("特徵向量",v)
#3.
np.linalg.svd(array1)