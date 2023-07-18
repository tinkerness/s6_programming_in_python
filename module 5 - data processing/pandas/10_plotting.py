import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("text.csv")
df.plot()
plt.show()