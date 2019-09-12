import pandas as pd
from sklearn.utils import shuffle

# 这是一个测试混淆数据集方法的脚本
df = pd.read_csv("train_data.csv", names=["1", "2", "3"])
df.sample(frac=1)  # 打乱顺序
df.sample(frac=1).reset_index(drop=True)  # 打乱顺序，重建索引
# print(df)
df = shuffle(df)  # 同df.sample(frac=1)
print(df)
print(df["1"])
