#!/usr/bin/env python3
# import roslib; roslib.load_manifest('Phoebe')
import rospy
import csv  
import pandas as pd
from nav_msgs.msg import Odometry
# df1 = pd.DataFrame[{"x":[0],"y":[0]}]
data1=[]
data2=[]
def odometryCb(msg):
    a = msg.pose.pose.position.x
    b = msg.pose.pose.position.y
    
    data1.append(a)
    data2.append(b)
    data = {
        "x": data1, "y":data2
    }
    df = pd.DataFrame(data)
    print("sub: ",df)
    
    # df.to_csv('/home/tu2022/Downloads/countries.csv', sep='\t', encoding='utf-8')
    df.to_csv("/home/tu2022/lego4/src/LeGO-LOAM/LeGO-LOAM/file_txt/odom1.csv")
    # with open('/home/tu2022/Downloads/countries.csv', 'w', encoding='UTF8') as f:
    #     writer = csv.writer(f)

    #     # write the header
    #     writer.writerow(df)

if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node 
    rospy.Subscriber('/laser_odom_to_init',Odometry,odometryCb)
    
    rospy.spin()