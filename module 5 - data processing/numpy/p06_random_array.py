import numpy as np

# generate 1D array of 5 random integers between 0 and 9
integer_array = np.random.randint(0, 10, 5)
print("1D Random Integer Array:\n",integer_array)

# generate 1D array of 5 random numbers between 0 and 1
float_array = np.random.rand(5)
print("\n1D Random Float Array:\n",float_array)

# generate 2D array of shape (3, 4) with random integers
result = np.random.randint(0, 10, (3,4))
print("\n2D Random Integer Array:\n",result)
