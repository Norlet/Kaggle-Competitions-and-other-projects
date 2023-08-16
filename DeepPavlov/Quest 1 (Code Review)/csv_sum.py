import pandas as pd

df = pd.read_csv("data.csv", sep=",", header=None)
print(df.values.sum()==10)
