import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[6, 7], [8, 9]])
print(A.ndim)
print(B.ndim)
print(A.shape)
print(B.shape)

# element operations
add = np.add(A, B)
print(add)
diff = np.subtract(A, B)
print(diff)
product = np.multiply(A, B)
print(product)
div = np.divide(A, B)
print(div)
# identity matrix
I = np.identity(3)
print(I)
# null matrix
N = np.zeros(3)
print(N)
# matrix with all ones
P = np.ones((3, 3))
print(P)
#matrix multipliction
C=np.matmul(A,B)
print(C)
#dot product
D=np.dot(A,B)
print(D)
#inverse of matrix
IN= np.linalg.inv(A)
print(IN)
#Determinant of matrix
DET=np.linalg.det(A)
print(DET)
#transpose of a matrix
T=np.transpose(B)
print(T)