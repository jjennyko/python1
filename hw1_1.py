import numpy as np

a = np.arange(16).reshape(8, 2)
print(a)
print('ndim: ', a.ndim)
print('shape: ', a.shape)
print('size: ', a.size)
print('dtype: ', a.dtype)
print('itemsize: ', a.itemsize)
print('data: ', a.data)
print('list(a): ', list(a))
print('tolist(): ', a.tolist())