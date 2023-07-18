import matplotlib.pyplot as plt

#define the figure size
plt.figure(figsize=(7,7))

x = [25,30,45,10]
labels = ["S", "A+", "A", "B+"]

plt.pie(x,labels=labels)
plt.show()