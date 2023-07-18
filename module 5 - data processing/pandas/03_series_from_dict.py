#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

data = {'a' : 0., 'b' : 1., 'c' : 2.}
# dictionary keys are taken in a sorted order to construct index
# s = pd.Series(data)

# Index order is persisted and the missing element is filled with NaN (Not a Number).
s = pd.Series(data,index=['b','c','d','a'])

print(s)