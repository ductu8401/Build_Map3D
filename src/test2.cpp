#include "utility.h"
#include "std_msgs/Float64MultiArray.h"

void get_data(const std_msgs::Float64MultiArray::ConstPtr& msg)
{
    // cout<<"data:"<<msg->data.at(0)<<","<<msg->data.at(1)<<","<<msg->data.at(2)<<endl;
    float end_time = ros::Time::now().toSec();
    float a = msg->data.at(0);
    cout<<"TIME:"<<(end_time-a)<<endl;
}
// void get_data1(const std_msgs::Float32::ConstPtr& msg1)
// {
//     cout<<"verticalAngle: "<<msg1->data<<endl;
// }
// void get_data2(const std_msgs::Float32::ConstPtr& msg2)
// {
//     // cout<<"horizonAngle: "<<msg2->data<<endl;
// }
int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "test2");
  ros::NodeHandle n;
  ROS_INFO("\033[1;32m---->\033[0m TEST2 START.");
  ros::Subscriber sub = n.subscribe("/time/data", 1, get_data);
//   ros::Subscriber sub1 = n.subscribe("/test/data1", 1, get_data1);
//   ros::Subscriber sub2 = n.subscribe("/test/data2", 1, get_data2);
  ros::spin();

  return 0;
}