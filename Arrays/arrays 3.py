import numpy as np
from sys import getsizeof as size
#multi dimensional arrays
A=np.array([[1,2,3],[4,5,6],[7,8,9],[41,65,12]])
X=np.array([1,2,3,4])
print(A.ndim)
print(A)
#shape of 2D array
print(A.shape)
print(A.dtype)
print(size(np.array([])))
print(size(A))
print \
"""#chaniging size of elements
B=np.array(A,np.int8)
print(B.dtype)
print(size(np.array([])))
print(size(B)"""
#accessing elements in array
print(A[2,1])
print(A[3,2])
#slicing(first two rows)
print(A[:,:])
print(A[:2,:3])
print(A[2:,1:3])