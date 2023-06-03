import matplotlib.pyplot as plt
import pandas as pd
import random
total1=0
df1 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/1.csv')
y1 = df1["imageProjection"].mean()
y1=y1*1000

# y = df.iloc[:,1]
df2 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/2.csv')
y2 = df2["Feature"].mean()
y2=y2*1000

df3 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/3.csv')
y3 = df3["mapOptization"].mean()
y3=y3*1000

df4 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/4.csv')
y4 = df4["transform"].mean()
y4=y4*1000
print(y1)
print(y2)
print(y3)
print(y4)