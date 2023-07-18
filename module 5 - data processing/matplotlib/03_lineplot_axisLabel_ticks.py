import matplotlib.pyplot as plt

years = [2000,2004,2008,2012,2016]
scores = [20,10,40,20,60]
hours = [10,25,20,25,15]

plt.title("Progress",color="red")
plt.plot(years,scores,'g-o',label="scores")
plt.plot(years,hours,'b-x',label="hours")

plt.xlabel("years")
plt.ylabel("progress", rotation=90)

# Customize the y-axis tick marks
# Set specific tick positions & their labels
plt.yticks([0, 10, 20, 30, 40, 50, 60],['0', '10', '20', '30', '40', '50', '60'])

plt.legend()
plt.show()