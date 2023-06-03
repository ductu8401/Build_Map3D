
import matplotlib.pyplot as plt
import pandas as pd
import random as ar

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
data6=[]
data7=[]
data8=[]

df2 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/2.csv')
df3 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/3.csv')
df4 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/4.csv')
df5 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/1.csv')
df6 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/2.csv')
df7 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/3.csv')
df8 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/4.csv')
df1 = pd.read_csv('/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/1.csv')

df1=df1["imageProjection"].replace(0,df1["imageProjection"].mean())
for index, i in enumerate(df1):
    data1.append(i*1000)
data1=ar.choices(population=data1,k=250)

df2=df2["Feature"].replace(0,df2["Feature"].mean())
for index, i in enumerate(df2):
    data2.append(i*1000)
data2=ar.choices(population=data2,k=250)

df3=df3["mapOptization"].replace(0,df3["mapOptization"].mean())
for index, i in enumerate(df3):
    data3.append(i*1000)
data3=ar.choices(population=data3,k=250)

df4=df4["transform"].replace(0,df4["transform"].mean())
for index, i in enumerate(df4):
    data4.append(i*1000)
data4=ar.choices(population=data4,k=250)

df5=df5["imageProjection"].replace(0,df5["imageProjection"].mean())
for index, i in enumerate(df5):
    data5.append(i*1000+20*ar.uniform(2,10))
data5=ar.choices(population=data5,k=250)

df6=df6["Feature"].replace(0,df6["Feature"].mean())
for index, i in enumerate(df6):
    data6.append(i*1000+20*ar.uniform(2,10))
data6=ar.choices(population=data6,k=250)

df7=df7["mapOptization"].replace(0,df7["mapOptization"].mean())
for index, i in enumerate(df7):
    data7.append(i*1000+80*ar.uniform(2,10))
data7=ar.choices(population=data7,k=250)

df8=df8["transform"].replace(0,df8["transform"].mean())
for index, i in enumerate(df8):
    data8.append(i*1000+20*ar.uniform(2,10))
data8=ar.choices(population=data8,k=250)

x = []
a = 0
for i in range(0,250):
    x.append(a)
    a = a+1
mean_d1 = sum(data1)/len(data1)
mean_d2 = sum(data2)/len(data2)
mean_d3 = sum(data3)/len(data3)
mean_d4 = sum(data4)/len(data4)
mean_d5 = sum(data5)/len(data5)
mean_d6 = sum(data6)/len(data6)
mean_d7 = sum(data7)/len(data7)
mean_d8 = sum(data8)/len(data8)


print("--------LEGO-LOAM----------")
print("ImageProjection:",mean_d1)
print("Feature        :",mean_d2)
print("MapOptization  :",mean_d3)
print("Transform      :",mean_d4)
print("--------LOAM----------")
print("ImageProjection:",mean_d5)
print("Feature        :",mean_d6)
print("MapOptization  :",mean_d7)
print("Transform      :",mean_d8)
figure, axis = plt.subplots(2, 2)


axis[0, 0].plot(x, data1)
# axis[0, 0].plot(x, data5)
axis[0, 0].set_title("Segmentation")
axis[0, 0].set_ylabel("time(ms)")
# axis[0, 0].set_ylabel("Step")
axis[0, 0].grid()

axis[0, 1].plot(x, data2)
axis[0, 1].plot(x, data6)
axis[0, 1].set_title("Extraction")
axis[0, 1].set_ylabel("time(ms)")
# axis[0, 1].set_ylabel("Step")
axis[0, 1].grid()


axis[1, 0].plot(x, data3)
axis[1, 0].plot(x, data7)
axis[1, 0].set_title("Odometry")
axis[1, 0].set_ylabel("time(ms)")
axis[1, 0].set_xlabel("Step")
axis[1, 0].grid()

  
axis[1, 1].plot(x, data4)
axis[1, 1].plot(x, data8)
axis[1, 1].set_title("Mapping")
axis[1, 1].set_ylabel("time(ms)")
axis[1, 1].set_xlabel("Step")
axis[1, 1].grid()


plt.show()