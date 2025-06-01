import numpy as np

arr = np.array([1,2,3,4,5,6])
new = arr.reshape(2,3)
print(new)
# reshaping donot create a copy, it returns a view