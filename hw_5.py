#1.
import numpy as np 
a=np.arange(0,11)
b=[]
for i in a :
    if i>=3 and i<=6 :
        b.append(i*-1)
    else :
        b.append(i)
print(b)
#2.
a = np.random.rand( 6 )
b =(a[a > 0.5])
print(b)
print(len(b))