#1.
import numpy as np
a= np.arange(6)
print(a)
print(a.sum())
print(np.sum(a))
print(sum(a))

#2. 
A = np.random.random((5,5))
print(A)
B = (A-A.min())/(A.max()-A.min())
print(B)

#3.
c = np.random.randint(1,100,10)
c[c.argmax()] = -1
print(c)
