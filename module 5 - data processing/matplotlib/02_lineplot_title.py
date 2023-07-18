import matplotlib.pyplot as plt

years = [2000,2004,2008,2012,2016]
scores = [20,10,40,20,60]
hours = [10,25,20,25,15]

# chart title - text,clr,size,vertical margin,position
plt.title("Progress",color="red",size=16,y=1.05, loc="center")
plt.plot(years,scores,'g-o',label="scores")
plt.plot(years,hours,'b-x',label="hours")

plt.legend()
plt.show()
