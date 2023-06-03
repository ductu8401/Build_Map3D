#!/usr/bin/env python3
import rospy
import pandas as pd
from std_msgs.msg import Float32
# df1 = pd.DataFrame[{"x":[0],"y":[0]}]
data1=[]
data2=[]
data3=[]
data4=[]
def time_sec(msg):
    a = msg.data
    data1.append(a)
    data = {
        "imageProjection": data1
    }
    df = pd.DataFrame(data)
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/9.csv")  
def time_sec2(msg):
    b = msg.data
    data2.append(b)
    data = {
        "Feature": data2
    }
    df = pd.DataFrame(data)
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/6.csv")  
def time_sec3(msg):
    c = msg.data
    data3.append(c)
    data = {
        "mapOptization": data3
    }
    df = pd.DataFrame(data)
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/7.csv")  
def time_sec4(msg):
    d = msg.data
    data4.append(d)
    data = {
        "transform": data4
    }
    df = pd.DataFrame(data)
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/8.csv")  

if __name__ == "__main__":
    rospy.init_node('data1', anonymous=True) #make node 
    rospy.Subscriber('/test/data1',Float32,time_sec)
    rospy.Subscriber('/test/data2',Float32,time_sec2)
    rospy.Subscriber('/test/data3',Float32,time_sec3)
    rospy.Subscriber('/test/data4',Float32,time_sec4)
    rospy.spin()