import matplotlib.pyplot as plt
import numpy as np

# Generate random data using np.random.normal() function
# create array of 250 random values, mean of 270, standard deviation of 50
x = np.random.normal(270, 50, 250)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Create a histogram plot
plt.hist(x)
# Display the plot
plt.show()