import pandas as pd
import numpy as np

s = pd.Series(5, index=[0, 1, 2, 3])
# value will be repeated to match the length of index
print(s)