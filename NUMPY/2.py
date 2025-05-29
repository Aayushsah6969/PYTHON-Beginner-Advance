import numpy as np

#Range of numbers 
aar=np.arange(0, 12, 2) #start, stop, step
print("Arrange: ",aar)


# Evenly spaced numbers
arr4 = np.linspace(0, 1, 5)  # start, end, number of samples
print("Linspace:", arr4)


# Constant value
full_arr = np.full((2, 2), 7)
print("Full array:\n", full_arr)

#grayscale image simulation
image=np.random.randint(0, 256, size=(5,5))
print("Gray scale Image:\n", image)