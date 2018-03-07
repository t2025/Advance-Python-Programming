import numpy as np
#Matrix 1
a=np.matrix('1,2;3,4')
print("A=",a)
#matrix 2
b= np.matrix('5,6;7,8')
print("B=",b)
#combined matrix
c=np.concatenate((a,b))
print("C=",c)
