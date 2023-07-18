import numpy as np

low = int(input("enter lower range : "))
high = int(input("enter higher range : "))

random_integer = np.random.randint(low,high)
print("random integer = ",random_integer)

# generate random float-point number between 0 and 1
random_float = np.random.rand()
print("random float = ",random_float)

# Choose Random Number from NumPy Array 
arr = np.array([1,2,3,4,5])
random_choice = np.random.choice(arr)
print("random choice = ",random_choice)