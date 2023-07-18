import pandas as pd
my_dict = {
    'name' : ["a", "b", "c", "d", "e","f", "g"],
    'age' : [20,27, 35, 55, 18, 21, 35],
    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]
}

# df = pd.DataFrame(my_dict)
df = pd.DataFrame(my_dict, index=[1,2,3,4,5,6,7])
df.to_csv("text.csv",index=False)

print(df)