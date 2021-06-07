#1
import numpy as np
a=np.arange(15)
print('type(a)資料類型: ', type(a))
print('a.dtype陣列中的資料型態: ', a.dtype)
#2
def is_dtype(a,t):
    return a.dtype is t
a=np.random.randint(10, size=6) 
# test1
print(is_dtype(a, 'int')) 
# test2
print(is_dtype(a, np.int)) 

# test3
print(is_dtype(a, np.dtype('int')))

#3
def is_dtype(a, t):
    return a.dtype is t  # 改為 a.dtype == t 才對 

def is_dtype(a, t):
    return type(a) == np.dtype(t) # type 本不等於 dtype

def is_dtype(a, t):
    return type(a) is np.dtype(t) # type 本不等於 dtype

# 進階
array1 = np.array(range(30))
print(array1)
array2 = array1.reshape((5,6),order="F")
print(array2)
print(np.where(array2 % 6 == 1))