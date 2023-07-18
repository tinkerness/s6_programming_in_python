import pandas as pd

usecols = ['name','age']
employee = pd.read_csv("text.csv",index_col=0,usecols=usecols)

# View the last 5 rows
print(employee.tail())