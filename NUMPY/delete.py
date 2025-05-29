import numpy as np

arr1=np.array([1,2,3,4])

arr2=np.delete(arr1, 0)
print(arr2)
print(arr1)

arr2d=np.array([[1,2,3],[4,5,6]])
arr2dn=np.delete(arr2d, 0, axis=0)
print(arr2dn)