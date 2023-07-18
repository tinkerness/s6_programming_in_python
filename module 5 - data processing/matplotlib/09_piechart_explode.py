import matplotlib.pyplot as plt

plt.figure(figsize = (7,7))
x = [25,30,45,10]
labels = ["S", "A+", "A", "B+"]

myexplode = [0, 0, 0, 0.2]

plt.pie(x,labels = labels,startangle = 90,explode = myexplode)
plt.show()