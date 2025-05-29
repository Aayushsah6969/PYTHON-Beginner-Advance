import numpy as np

arr = np.array([1,2,3,6,76,89,89])
print(arr)
# Store the result in arr variable
arr = np.insert(arr, 2, 900, axis=None)
print(arr)