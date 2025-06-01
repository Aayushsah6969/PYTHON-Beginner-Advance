# Aggregation functions in python numpy
import numpy as np

arr=np.array([12,45,6,89,100,34,8])

print("Sum of all elements in array is: " ,np.sum(arr))
print("Mean of data ", np.mean(arr))
print("Minimum: ", np.min(arr))
print("Maximun: ",np.max(arr))
print("Standard deviation: ",np.std(arr))
print("variance: ",np.var(arr))
print(np.shape(arr))
print(np.size(arr))