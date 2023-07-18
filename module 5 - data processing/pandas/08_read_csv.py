import pandas as pd
# Read the CSV file

# default behavior of pandas is to add an initial index to the dataframe 
# employee = pd.read_csv("text.csv")

# explicitly specify what column to make as the index to the read_csv function by setting the index_col parameter
employee = pd.read_csv("text.csv",index_col=0)

# View the first 5 rows
print(employee.head())