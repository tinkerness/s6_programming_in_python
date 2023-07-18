import matplotlib.pyplot as plt
import numpy as np

x = np.array([100,90,80,70,60,50,40])
y = np.array([12, 27, 20, 10, 20, 10, 5])

plt.title("Python Programing")
plt.xlabel("No of Students")
plt.ylabel("Marks")

plt.scatter(x,y)
plt.show()