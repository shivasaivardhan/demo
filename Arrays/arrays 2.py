import numpy as np
from sys import getsizeof as size
#delaring list
A=[1,2,3,4,5,6]
print(A)
print(type(A))
#converting to array
B=np.array(A)
print(type(B))
#size of each variable(bits)
print(size(A))#36+6*4
print(size(B))#48+6*4
#size of empty array and empty list(bits)
print(size([]))
print(size(np.array([])))
#In array or list each element takes 4 bits
#data type of each element in array
print(B.dtype)
#optimising the memory allocted to int 16,32,64(changing size)
B=np.array(A,np.int8)#only for arrays not list
print(size(B))

#comparing operations of arrays and list
C=B/2 #arrays
print(C)
#D=A/2 #list throws error
#print(D)
D=list(i/2 for i in A)
print(D)
