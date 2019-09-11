import pandas as pd
from sklearn.utils import shuffle


df = pd.read_csv("train_data.csv", names=["1", "2", "3"])
# print(df)
df = shuffle(df)
print(df)
print(df["1"])
