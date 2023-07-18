import matplotlib.pyplot as plt
import numpy as np

x = np.array(["S", "A+", "A", "B+"])
y = np.array([12, 27, 20, 10])

plt.title("Python Programing")
# invert
plt.xlabel("No of Students")
plt.ylabel("Grades")

plt.barh(x,y,color="pink")
plt.show()