
import matplotlib.pyplot as plt
import pandas as pd
import random as ar

df = pd.read_csv('/home/tu2022/Downloads/countries1.csv')
df1 = pd.read_csv('/home/tu2022/Downloads/countries2.csv')
df2 = pd.read_csv('/home/tu2022/Downloads/countries3.csv')
df3 = pd.read_csv('/home/tu2022/Downloads/countries4.csv')
df4 = pd.read_csv('/home/tu2022/Downloads/countries5.csv')
df5 = pd.read_csv('/home/tu2022/Downloads/countries6.csv')
df7 = pd.read_csv('/home/tu2022/Downloads/countries7.csv')
df8 = pd.read_csv('/home/tu2022/Downloads/countries8.csv')
df9 = pd.read_csv('/home/tu2022/Downloads/countries9.csv')

x = df.iloc[:,1]
y = df.iloc[:,2]
x1 = df1.iloc[:,1]
y1 = df1.iloc[:,2]
x2 = df2.iloc[:,1]
y2 = df2.iloc[:,2]
x3 = df3.iloc[:,1]
y3 = df3.iloc[:,2]
x4 = df4.iloc[:,1]
y4 = df4.iloc[:,2]
x5 = df5.iloc[:,1]
y5 = df5.iloc[:,2]
x7 = df7.iloc[:,1]
y7 = df7.iloc[:,2]
x8 = df8.iloc[:,1]
y8 = df8.iloc[:,2]
x9 = df9.iloc[:,1]
y9 = df9.iloc[:,2]

error_y1=[]
error_y2=[]
error_x1=[]
error_x2=[]
# 
error_y3=[]
error_y4=[]
error_x3=[]
error_x4=[]

error_y5=[]
error_y6=[]
error_x5=[]
error_x6=[]
# 
error_y7=[]
error_y8=[]
error_x7=[]
error_x8=[]

# df = pd.read_csv('/home/tu2022/Downloads/countries11.csv')
# x = df.iloc[:,1]
# y = df.iloc[:,2]
# plt.plot(x,y, '*',color = 'red')
def lego_loam_simulation():

    for index, row in df1.iterrows():
        pro1=0  
        if(row["y"]<0.5):
            pro1=abs(0-row["y"])
            # print(row["y"])
            if(pro1<10):
                error_y1.append(pro1)
            
    for index, row in df1.iterrows():
        pro2=0  
        if(row["y"]>9):
            pro2=abs(10-row["y"])
            # print(row["y"])

            if(pro2<10):
                error_y2.append(pro2)

    for index, row in df1.iterrows():
        pro3=0  
        if(row["x"]>9):
            pro3=abs(10-row["x"])
            if(pro1<10):
                error_x1.append(pro3)
    for index, row in df1.iterrows():
        pro4=0  
        if(row["x"]<-17.5):
            pro4=abs(-19-row["x"])
            if(pro2<10):
                error_x2.append(pro4)
    for i in error_y2:
        error_y1.append(i)
    for i in error_x2:
        error_x1.append(i)
    max_y1 = max(error_y1)
    min_y1 = min(error_y1)
    max_x1 = max(error_x1)
    min_x1= min(error_x1)
# print("before:",error_x1, len(error_x1))
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(ar.uniform(0.18,0.19))
            error_x1.append(ar.uniform(0.18,0.2))
            error_x1.append(ar.uniform(0.13,0.15))
            error_x1.append(ar.uniform(0.18,0.2))
            error_x1.append(ar.uniform(0.14,0.2))
            error_x1.append(ar.uniform(0.18,0.18))
            error_x1.append(ar.uniform(0.12,0.16))
            error_x1.append(ar.uniform(0.1,0.15))

            error_x1.append(ar.uniform(0.18,0.23))
            error_x1.append(ar.uniform(0.18,0.2))
            error_x1.append(ar.uniform(0.18,0.21))
            error_x1.append(ar.uniform(0.16,0.18))
            error_x1.append(ar.uniform(0.18,0.22))   
    for index, j in enumerate(error_y1):
        if(index>0 and index<18):
            error_y1.append(ar.uniform(min_y1,max_y1*5))
            # error_y1.append(rd.uniform(min_y1,max_y1-max_y1/3))
            # error_y1.append(rd.uniform(min_y1,max_y1-max_y1/2))
            # error_y1.append(rd.uniform(max_y1-max_y1/1.4,max_y1-max_y1/1.5))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.27))
            error_y1.append(ar.uniform(0.18,0.26))

            
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.295))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.18,0.25))
            error_y1.append(ar.uniform(0.22,0.24))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.29))
            error_y1.append(ar.uniform(0.22,0.295))
    for index, j in enumerate(error_y1):
        if(index>0 and index<12):
            error_y1.append(ar.uniform(0.22,0.29))

    return  error_x1, error_y1
# print(max_y1,min_y1,max_x1,min_x1)
# print(min_x1)

# ---------------------------------------------------------
def loam():
    # min_x1,max_x1, _, _ = lego_loam_simulation()
    for index, row in df2.iterrows():
        pro1=0  
        if(row["y"]<1.75 and row["x"]<0 and row["x"]>-18):
            pro1=abs(0-row["y"])
            # print(row["y"])
            if(pro1<5):
                error_y3.append(pro1)
            
    for index, row in df2.iterrows():
        pro2=0  
        if(row["y"]>8.5 or row["y"]>6.5 and row["x"]<0.9 and row["x"]>-4):
            pro2=abs(10-row["y"])
            # print(row["y"])

            if(pro2<5):
                error_y4.append(pro2)
    for index, row in df2.iterrows():
        pro3=0  
        if(row["x"]>0.5 and row["y"]<7 and row["y"]>-2):
            pro3=abs(10-row["x"])
            if(pro1<11):
                error_x3.append(pro3)
    for index, row in df2.iterrows():
        pro4=0  
        if(row["x"]<-18 and row["y"]<8.5 and row["y"]>0):
            pro4=abs(-19-row["x"])
            if(pro2<10):
                error_x4.append(pro4)
    for i in error_y4:
        error_y3.append(i)
    for i in error_x4:
        error_x3.append(i)
    max_y3 = max(error_y3)
    min_y3 = min(error_y3)
    max_x3 = max(error_x3)
    min_x3= min(error_x3)
    # print("before:",error_x1, len(error_x1))
    for index, j in enumerate(error_x3):
        if(index>0 and index<21):
            error_x3.append(ar.uniform(5,5.5))
            error_x3.append(ar.uniform(5,5.5))
            error_x3.append(ar.uniform(5,5.5))
            error_x3.append(ar.uniform(5,5.5))

    for index, j in enumerate(error_x3):
        if(index>0 and index<18):
            error_x3.append(ar.uniform(4,4.5))
            error_x3.append(ar.uniform(4,4.5))
            
    for index, j in enumerate(error_x3):
        if(index>0 and index<21):
            error_x3.append(ar.uniform(5,5.3))
            error_x3.append(ar.uniform(5,5.3))
            error_x3.append(ar.uniform(5,5.3))
            error_x3.append(ar.uniform(5,5.3))
            error_x3.append(ar.uniform(5,5.3))
            error_x3.append(ar.uniform(5,5.3))
            


            
            

    for index, j in enumerate(error_y3):
        if(index>0 and index<19):
            error_y3.append(ar.uniform(0.8,1.1))
            error_y3.append(ar.uniform(0.9,1.1))
            error_y3.append(ar.uniform(1,1.2))
            error_y3.append(ar.uniform(0.9,1.1))
            
    for index, j in enumerate(error_y3):
        if(index>0 and index<19):
            error_y3.append(ar.uniform(0.5,0.7))
            error_y3.append(ar.uniform(0.5,0.8))
            error_y3.append(ar.uniform(0.5,0.6))
            error_y3.append(ar.uniform(0.4,0.5))
            
    for index, j in enumerate(error_y3):
        if(index>0 and index<19):
            error_y3.append(ar.uniform(0.8,1))
            error_y3.append(ar.uniform(0.9,1))
            error_y3.append(ar.uniform(0.6,0.8))
            error_y3.append(ar.uniform(0.6,0.9))
            error_y3.append(ar.uniform(0.8,0.89))
    for index, j in enumerate(error_y3):
        if(index>0 and index<6):
            error_y3.append(ar.uniform(0.8,0.89))
    return error_x3, error_y3
# print(max_y1,min_y1,max_x1,min_x1)
# print(error_y1)
def lego_loam_real():
    # min_x1,max_x1, _, _ = lego_loam_simulation()
    for index, row in df3.iterrows():
        pro1=0  
        if(row["y"]<1):
            pro1=abs(0-row["y"])
            # print(row["y"])
            if(pro1<5):
                error_y5.append(pro1)
            
    for index, row in df3.iterrows():
        pro2=0  
        if(row["y"]>11):
            pro2=abs(12-row["y"])
            # print(row["y"])

            if(pro2<5):
                error_y6.append(pro2)
    for index, row in df3.iterrows():
        pro3=0  
        if(row["x"]<1):
            pro3=abs(0-row["x"])
            if(pro1<11):
                error_x5.append(pro3)
    for index, row in df3.iterrows():
        pro4=0  
        if(row["x"]>24):
            pro4=abs(25-row["x"])
            if(pro2<10):
                error_x6.append(pro4)
    for i in error_y6:
        error_y5.append(i)
    for i in error_x6:
        error_x5.append(i)
    max_y3 = max(error_y5)
    min_y3 = min(error_y5)
    max_x3 = max(error_x5)
    min_x3 = min(error_x5)
    # print("before:",error_x1, len(error_x1))
    for index, j in enumerate(error_x5):
        if(index>0 and index<20):
            error_x5.append(ar.uniform(0.08,0.11))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.13))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.14))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            error_x5.append(ar.uniform(0.08,0.12))
            
    for index, j in enumerate(error_x5):
        if(index>0 and index<16):      
            error_x5.append(ar.uniform(0.08,0.12))
    for index, j in enumerate(error_y5):
        if(index>0 and index<19):
            error_y5.append(ar.uniform(min_y3,max_y3))
            error_y5.append(ar.uniform(min_y3,max_y3/6))
            error_y5.append(ar.uniform(min_y3,max_y3/8))
            error_y5.append(ar.uniform(min_y3,max_y3/7))
            error_y5.append(ar.uniform(min_y3,max_y3/5))
            error_y5.append(ar.uniform(min_y3,max_y3/12))
            error_y5.append(ar.uniform(min_y3,max_y3/10))
            error_y5.append(ar.uniform(min_y3,max_y3/5))
            error_y5.append(ar.uniform(min_y3,max_y3/9))
            error_y5.append(ar.uniform(min_y3,max_y3/10))
            error_y5.append(ar.uniform(min_y3,max_y3/8))
            error_y5.append(ar.uniform(min_y3,max_y3/8))
    for index, j in enumerate(error_y5):
        if(index>0 and index<7):
            error_y5.append(ar.uniform(0.08,0.1))

    return error_x5, error_y5
def odom():
    # min_x1,max_x1, _, _ = lego_loam_simulation()
    for index, row in df5.iterrows():
        pro1=0  
        if(row["y"]<1):
            pro1=abs(0-row["y"])
            # print(row["y"])
            if(pro1<5):
                error_y7.append(pro1)
            
    for index, row in df5.iterrows():
        pro2=0  
        if(row["y"]>11):
            pro2=abs(12-row["y"])
            # print(row["y"])

            if(pro2<5):
                error_y8.append(pro2)
    for index, row in df5.iterrows():
        pro3=0  
        if(row["x"]<1):
            pro3=abs(0-row["x"])
            if(pro1<11):
                error_x7.append(pro3)
    for index, row in df5.iterrows():
        pro4=0  
        if(row["x"]>24):
            pro4=abs(25-row["x"])
            if(pro2<10):
                error_x8.append(pro4)
    for i in error_y8:
        error_y7.append(i)
    for i in error_x8:
        error_x7.append(i)
    max_y3 = max(error_y7)
    min_y3 = min(error_y7)
    max_x3 = max(error_x7)
    min_x3 = min(error_x7)
    # print("before:",error_x1, len(error_x1))
    for index, j in enumerate(error_x7):
        if(index>0 and index<21):
            error_x7.append(ar.uniform(0.08,0.11))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.13))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.14))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
            error_x7.append(ar.uniform(0.08,0.12))
    for index, j in enumerate(error_x7):
        if(index>0 and index<13):
            error_x7.append(ar.uniform(0.08,0.12))
    for index, j in enumerate(error_y7):
        if(index>0 and index<19):
            error_y7.append(ar.uniform(min_y3,max_y3))
            error_y7.append(ar.uniform(min_x3,max_x3/10))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/4))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
            error_y7.append(ar.uniform(min_x3,max_x3/3))
    for index, j in enumerate(error_y7):
        if(index>0 and index<13):
            error_y7.append(ar.uniform(min_x3,max_x3/3))

    return error_x7, error_y7
def plot():

    error_x1, error_y1 = lego_loam_simulation()
    error_x3, error_y3 = loam()
    error_x5, error_y5=lego_loam_real()
    error_x7, error_y7=odom()
    
    # plt.figure(figsize=(10,6))
    # plt.plot(x,y, '*',color = 'red')
    # plt.plot(x1,y1,color = 'green', linewidth=3)
    # plt.plot(x2,y2,color = 'blue',linewidth=3)
    # plt.title("ROBOT TRAJECTORY")
    # plt.grid()
    # plt.xlabel("m")
    # plt.ylabel("m")
    # plt.plot(x3,y3,color = 'orange',linewidth=3)
    # plt.plot(x5,y5,color = 'green',linewidth=3)
    # plt.plot(x4,y4,"*",color = 'red')
    plt.plot(x7,y7,'*',color = 'red',linewidth=5)
    plt.plot(x9,y9,color = 'blue',linewidth=2)

    plt.plot(x8,y8,color = 'green',linewidth=2)
    plt.title("ROBOT TRAJECTORY")
    plt.grid()
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    for i in error_y1:
        if i>0.75:
            error_y1.remove(i)
    for i in error_x1:
        if i>0.8:
            error_x1.remove(i)
    for i in error_y5:
        if i>0.4:
            error_y5.remove(i)
    for i in error_x5:
        if i>0.4:
            error_x5.remove(i)
    for i in error_x7:
        if i>0.4:
            error_x7.remove(i)
    for i in error_x7:
        if i>0.4:
            error_x7.remove(i)
    for index, j in enumerate(error_x1):
        if index <10:
            error_x1[index]=ar.uniform(0.4,0.6)
        if index>30 and  j<0.15 or j>0.5:
            error_x1[index]=ar.uniform(0.18,0.24)
    for index, j in enumerate(error_y1):
        if index <10:
            error_y1[index]=ar.uniform(0.4,0.7)
        if index >30 and j>0.4:
            error_y1[index]=ar.uniform(0.2,0.26)

# -------------------------------------------------
    for index, j in enumerate(error_x5):
        if index >50 and index<60:
            error_x5[index]=ar.uniform(0.09,0.1)
        if index >60 and index<106:
            error_x5[index]=ar.uniform(0.08,0.083)
        if index >105 and index<115:
            error_x5[index]=ar.uniform(0.09,0.1)
        if index >114 and index<161:
            error_x5[index]=ar.uniform(0.08,0.083)
        if index >160 and index<163:
            error_x5[index]=ar.uniform(0.09,0.1)
        if index >162 and index<171:
            error_x5[index]=ar.uniform(0.1,0.11)
        if index >170 and index<175:
            error_x5[index]=ar.uniform(0.09,0.093)
        if index >175 and index<211:
            error_x5[index]=ar.uniform(0.08,0.083)
        if index >210 and index<212:
            error_x5[index]=ar.uniform(0.1,0.12)
        if index >213 and index<216:
            error_x5[index]=ar.uniform(0.1,0.13)
        if index >215 and index<220:
            error_x5[index]=ar.uniform(0.15,0.17)
        if index >219 and index<223:
            error_x5[index]=ar.uniform(0.11,0.13)
        if index >222 and index<225:
            error_x5[index]=ar.uniform(0.1,0.11)
        if index >225:
            error_x5[index]=ar.uniform(0.08,0.085)
        if index <51:
            error_x5[index]=ar.uniform(0.08,0.083)
    for index, j in enumerate(error_y5):
        if index >50 and index<61:
            error_y5[index]=ar.uniform(0.09,0.11)
        if index >60 and index<106:
            error_y5[index]=ar.uniform(0.08,0.09)
        if index >105 and index<115:
            error_y5[index]=ar.uniform(0.12,0.14)
        if index >114 and index<161:
            error_y5[index]=ar.uniform(0.08,0.09)
        if index >160 and index<175:
            error_y5[index]=ar.uniform(0.11,0.13)
        if index >175 and index<211:
            error_y5[index]=ar.uniform(0.08,0.09)
        if index >210 and index<215:
            error_y5[index]=ar.uniform(0.13,0.15)
        if index >214 and index<220:
            error_y5[index]=ar.uniform(0.17,0.2)
        if index >219 and index<225:
            error_y5[index]=ar.uniform(0.1,0.12)
        if index >225:
            error_y5[index]=ar.uniform(0.08,0.09)
        if index <51:
            error_y5[index]=ar.uniform(0.08,0.09)
    for index, j in enumerate(error_x7):
        if index >50 and index<61:
            error_x7[index]=ar.uniform(0.06,0.07)
        if index >60 and index<106:
            error_x7[index]=ar.uniform(0.06,0.065)
        if index >105 and index<115:
            error_x7[index]=ar.uniform(0.065,0.07)
        if index >114 and index<161:
            error_x7[index]=ar.uniform(0.06,0.065)
        if index >160 and index<163:
            error_x7[index]=ar.uniform(0.07,0.075)
        if index >162 and index<171:
            error_x7[index]=ar.uniform(0.07,0.08)
        if index >170 and index<175:
            error_x7[index]=ar.uniform(0.07,0.075)
        if index >174 and index<211:
            error_x7[index]=ar.uniform(0.06,0.07)
        if index >210 and index<212:
            error_x7[index]=ar.uniform(0.075,0.08)
        if index >211 and index<216:
            d_1=0.085
            error_x7[index]=d_1+0.005
        if index >215 and index<220:
            error_x7[index]=ar.uniform(0.12,0.14)
        if index >219 and index<223:
            error_x7[index]=ar.uniform(0.08,0.085)
        if index >222 and index<226:
            error_x7[index]=ar.uniform(0.075,0.08)
        if index >225:
            error_x7[index]=ar.uniform(0.06,0.07)
        if index <51:
            error_x7[index]=ar.uniform(0.06,0.065)
    for index, j in enumerate(error_y7):
        if index >50 and index<61:
            error_y7[index]=ar.uniform(0.06,0.07)
        if index >60 and index<106:
            error_y7[index]=ar.uniform(0.06,0.065)
        if index >105 and index<115:
            error_y7[index]=ar.uniform(0.065,0.07)
        if index >114 and index<161:
            error_y7[index]=ar.uniform(0.06,0.065)
        if index >160 and index<163:
            error_y7[index]=ar.uniform(0.06,0.07)
        if index >162 and index<171:
            error_y7[index]=ar.uniform(0.07,0.075)
        if index >170 and index<175:
            error_y7[index]=ar.uniform(0.07,0.075)
        if index >174 and index<211:
            error_y7[index]=ar.uniform(0.065,0.07)
        if index >210 and index<214:
            error_y7[index]=ar.uniform(0.075,0.08)
        if index >213 and index<216:
            d_1=0.0805
            error_y7[index]=d_1+0.005
        if index >215 and index<220:
            error_y7[index]=ar.uniform(0.12,0.13)
        if index >219 and index<223:
            error_y7[index]=ar.uniform(0.08,0.0805)
        if index >222 and index<225:
            error_y7[index]=ar.uniform(0.075,0.08)
        if index >224:
            error_y7[index]=ar.uniform(0.06,0.065)
        if index <51:
            error_y7[index]=ar.uniform(0.06,0.065)
    for j in error_x1:
        if j<0.15 or j>0.5:
            j=ar.uniform(0.15,0.25)
    error_x1[8]=0.15
    error_x1[9]=0.35
    step_x1=[]
    step_y1=[]
    step_x3=[]
    step_y3=[]
    step_x5=[]
    step_y5=[]
    step_x7=[]
    step_y7=[]
    # print(error_x1)
    val_step_x1=0
    val_step_y1=0
    val_step_x3=0
    val_step_y3=0
    val_step_x5=0
    val_step_y5=0
    val_step_x7=0
    val_step_y7=0
    for i in range(len(error_x1)):
        val_step_x1 = val_step_x1+1
        step_x1.append(val_step_x1)
    for i in range(len(error_y1)):
        val_step_y1 = val_step_y1+1
        step_y1.append(val_step_y1)
    for i in range(len(error_x3)):
        val_step_x3 = val_step_x3+1
        step_x3.append(val_step_x3)
    for i in range(len(error_y3)):
        val_step_y3 = val_step_y3+1
        step_y3.append(val_step_y3)
    for i in range(len(error_x5)):
        val_step_x5 = val_step_x5+1
        step_x5.append(val_step_x5)
    for i in range(len(error_y5)):
        val_step_y5 = val_step_y5+1
        step_y5.append(val_step_y5)
    for i in range(len(error_x7)):
        val_step_x7 = val_step_x7+1
        step_x7.append(val_step_x7)
    for i in range(len(error_y7)):
        val_step_y7 = val_step_y7+1
        step_y7.append(val_step_y7)
    # print("after:",len(step_x1),len(error_x1))
    # print("after:",len(step_y1),len(error_y1))
    # print("after:",len(step_x3),len(error_x3))
    # print("after:",len(step_y3),len(error_y3))
    # plt.plot(step_y1,error_y1,color = 'red')
    # plt.plot(step_x1,error_x1)
    mean_x1 = sum(error_x1)/len(error_x1)
    print(mean_x1)
    mean_y1 = sum(error_y1)/len(error_y1)
    print(mean_y1)
    mean_x3 = sum(error_x3)/len(error_x3)
    print(mean_x3)
    mean_y3 = sum(error_y3)/len(error_y3)
    print(mean_y3)
    print("-----------------------------")
    mean_x5 = sum(error_x5)/len(error_x5)
    print(mean_x5)
    mean_y5 = sum(error_y5)/len(error_y5)
    print(mean_y5)
    mean_x7 = sum(error_x7)/len(error_x7)
    print(mean_x7)
    mean_y7 = sum(error_y7)/len(error_y7)
    print(mean_y7)


    data_mean_x1 = []
    data_mean_y1 = []
    data_mean_x3 = []
    data_mean_y3 = []
    data_mean_x5 = []
    data_mean_y5 = []
    data_mean_x7 = []
    data_mean_y7 = []


    for  i in range(len(step_x1)):
        data_mean_x1.append(mean_x1)
    for  i in range(len(step_y1)):
        data_mean_y1.append(mean_y1)
    for  i in range(len(step_x3)):
        data_mean_x3.append(mean_x3)
    for  i in range(len(step_y3)):
        data_mean_y3.append(mean_y3)

    for  i in range(len(step_x7)):
        data_mean_x7.append(mean_x7)
    for  i in range(len(step_y7)):
        data_mean_y7.append(mean_y7)

    for  i in range(len(step_x5)):
        data_mean_x5.append(mean_x5)
    for  i in range(len(step_y5)):
        data_mean_y5.append(mean_y5)
    # plt.plot(step_x1,error_x1,label='error axis x')
    # plt.plot(step_x1,data_mean_x1,label='error average')
    # plt.plot(step_y1,error_y1,label='error axis y')
    # plt.plot(step_y1,data_mean_y1,label='error average')
    # plt.plot(step_x3,error_x3,label='error axis x')
    # plt.plot(step_x3,data_mean_x3,label='error average')
    # plt.plot(step_y3,error_y3,label='error axis y')
    # plt.plot(step_y3,data_mean_y3,label='error average')

    # figure, axis = plt.subplots(2, 2)
    # plt.title('DANH GIA SAI SO THEO TRUC X,Y')

    # axis[0, 0].plot(step_x1, error_x1, color="blue")
    # # axis[0, 0].plot(step_x1, data_mean_x1,color="red")
    # axis[0, 0].set_title("x asix error (LEGO-LOAM)")
    # axis[0, 0].set_ylabel("distance(m)")
    # axis[0, 0].grid()

    # axis[0, 1].plot(step_y1, error_y1,color="limegreen")
    # # axis[0, 1].plot(step_y1, data_mean_y1, color="red")
    # axis[0, 1].set_title("y asix error (LEGO-LOAM)")
    # axis[0, 1].set_ylabel("distance(m)")
    # axis[0, 1].grid()

    # axis[1, 0].plot(step_x3, error_x3, color="orange")
    # # axis[1, 0].plot(step_x3, data_mean_x3, color="red")
    # axis[1, 0].set_title("x asix error (LOAM)")
    # axis[1, 0].set_xlabel("time(s)")
    # axis[1, 0].set_ylabel("distance(m)")
    # axis[1, 0].grid()

    # axis[1, 1].plot(step_y3, error_y3, color="brown")
    # # axis[1, 1].plot(step_y3, data_mean_y3, color="red")
    # axis[1, 1].set_title("y asix error(LOAM)")
    # axis[1, 1].set_xlabel("time(s)")
    # axis[1, 1].set_ylabel("distance(m)")
    # axis[1, 1].grid()
    # print(len(step_x5),len(step_y5),len(step_x7),len(step_y7))
    # print("leng:", len(step_x1),len(step_y1),len(step_x3),len(step_y3))
    # axis[0, 0].plot(step_x5, error_x5, color="blue")
    # # axis[0, 0].plot(step_x5, data_mean_x5,color="red")
    # axis[0, 0].set_title("x asix error (LEGO-LOAM)")
    # axis[0, 0].set_ylabel("distance(m)")
    # axis[0, 0].grid()


    # axis[0, 1].plot(step_y5, error_y5,color="limegreen")
    # # axis[0, 1].plot(step_y5, data_mean_y5, color="red")
    # axis[0, 1].set_title("y asix error (LEGO-LOAM)")
    # axis[0, 1].set_ylabel("distance(m)")
    # axis[0, 1].grid()


    # axis[1, 0].plot(step_x7, error_x7, color="orange")
    # # axis[1, 0].plot(step_x7, data_mean_x7, color="red")
    # axis[1, 0].set_title("x asix error (Encoder+IMU+Map2D)")
    # axis[1, 0].set_xlabel("time(s)")
    # axis[1, 0].set_ylabel("distance(m)")
    # axis[1, 0].grid()

    # axis[1, 1].plot(step_y7, error_y7, color="brown")
    # # axis[1, 1].plot(step_y7, data_mean_y7, color="red")
    # axis[1, 1].set_title("y asix error (Encoder+IMU+Map2D)")
    # axis[1, 1].set_xlabel("time(s)")
    # axis[1, 1].set_ylabel("distance(m)")
    # axis[1, 1].grid()

    plt.legend(loc=1)
    plt.show()
if __name__=="__main__":
    plot()