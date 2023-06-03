#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray
import pandas as pd
data_sub1=[]
data_sub2=[]
data_sub3=[]

def callback(data):

    # print(f'range: {data.data[0]:.2f}')
    data_sub1.append(data.data[0])
    data_sub2.append(data.data[1])
    data_sub3.append(data.data[2])
    dic_data = {"x": data_sub1, "y":data_sub2, "z": data_sub3}
    df = pd.DataFrame(dic_data)
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/5.csv")  

    # print(df)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sub_data', anonymous=True)

    rospy.Subscriber("/pose_data", Float64MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()