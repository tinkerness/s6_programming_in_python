# importing matplotlib module
import matplotlib.pyplot as plt

years = [2000,2004,2008,2012,2016]
scores = [20,10,40,20,60]
hours = [10,25,20,25,15]

# Function to plot
# basic - plt.plot(x,y)
# here - coordinates,colour-marker,label
plt.plot(years,scores,'g-o',label="scores")
plt.plot(years,hours,'b-x',label="hours")

# function to show the plot
plt.legend() #to show label
plt.show()
