#include "utility.h"
#include "std_msgs/Float64MultiArray.h"
// https://github.com/MNewBie/PCL-Notes
// https://robot.czxy.com/docs/pcl/
class test{
private:

    ros::NodeHandle nh;

    ros::Subscriber subLaserCloud;

    ros::Publisher pub;
    
    pcl::PointCloud<PointType>::Ptr laserCloudIn;
    pcl::PointCloud<PointXYZIR>::Ptr laserCloudInRing;

    cloud_msgs::cloud_info segMsg; // info of segmented cloud
    std_msgs::Header cloudHeader;
    std_msgs::Float64MultiArray msg;
    // std_msgs::Float32 msg1;
    // std_msgs::Float32 msg2;

public:
    test():
        nh("~"){

        subLaserCloud = nh.subscribe<sensor_msgs::PointCloud2>(pointCloudTopic, 1, &test::cloudHandler, this);
        pub = nh.advertise<std_msgs::Float64MultiArray>("/time/data",1);
        // pub1 = nh.advertise<std_msgs::Float32>("/test/data1",1);
        // pub2 = nh.advertise<std_msgs::Float32>("/test/data2",1);
        allocateMemory();
        resetParameters();
    }

    void allocateMemory(){

        laserCloudIn.reset(new pcl::PointCloud<PointType>());
        laserCloudInRing.reset(new pcl::PointCloud<PointXYZIR>());
    }

    void resetParameters(){
        laserCloudIn->clear();
    }

    ~test(){}

    void copyPointCloud(const sensor_msgs::PointCloud2ConstPtr& laserCloudMsg){

        cloudHeader = laserCloudMsg->header;
        // cloudHeader.stamp = ros::Time::now(); // Ouster lidar users may need to uncomment this line
        pcl::fromROSMsg(*laserCloudMsg, *laserCloudIn);
        // Remove Nan points
        std::vector<int> indices;
        pcl::removeNaNFromPointCloud(*laserCloudIn, *laserCloudIn, indices);
        // have "ring" channel in the cloud
        if (useCloudRing == true){
            pcl::fromROSMsg(*laserCloudMsg, *laserCloudInRing);
            if (laserCloudInRing->is_dense == false) {
                ROS_ERROR("Point cloud is not in dense format, please remove NaN points first!");
                ros::shutdown();
            }  
        }
    }
    
    void cloudHandler(const sensor_msgs::PointCloud2ConstPtr& laserCloudMsg){

        copyPointCloud(laserCloudMsg);
        projectPointCloud();
        resetParameters();
    }

    

    void projectPointCloud(){
        // range image projection
        float verticalAngle, horizonAngle, range;
        size_t rowIdn, columnIdn, index, cloudSize; 
        float begin_time;
        float data[3];
        PointType thisPoint;

        cloudSize = laserCloudIn->points.size();

        for (size_t i = 0; i < cloudSize; ++i){

            thisPoint.x = laserCloudIn->points[i].x;
            thisPoint.y = laserCloudIn->points[i].y;
            thisPoint.z = laserCloudIn->points[i].z;

            if (thisPoint.x >10 || thisPoint.y>10||thisPoint.z>10 ||thisPoint.x <-10 || thisPoint.y<-10||thisPoint.z<-10 )
            continue;
            // cout<<fixed<<setprecision(2)<<"x:"<<thisPoint.x<<"   y:"<<thisPoint.y<<"   z:"<<thisPoint.z<<endl;
            // find the row and column index in the iamge for this point

            verticalAngle = atan2(thisPoint.z, sqrt(thisPoint.x * thisPoint.x + thisPoint.y * thisPoint.y)) * 180 / M_PI;

            horizonAngle = atan2(thisPoint.x, thisPoint.y) * 180 / M_PI;

            range = sqrt(thisPoint.x * thisPoint.x + thisPoint.y * thisPoint.y + thisPoint.z * thisPoint.z);
            
            // rangeMat.at<float>(rowIdn, columnIdn) = range;
            // cout<<"---range pub: "<<range<<"---horizonAngle pub:"<<horizonAngle<<"---verticalAngle pub:"<<verticalAngle<<endl;
            // thisPoint.intensity = (float)rowIdn + (float)columnIdn / 10000.0;
            // cout<<fixed<<setprecision(2)<<"x:"<<thisPoint.x<<"   y:"<<thisPoint.y<<"   z:"<<thisPoint.z<<"  horizonAngle: "<<horizonAngle<<"   verticalAngle: "<<verticalAngle<<"   rowIdn: "<<rowIdn<<"   Range: "<<range<<endl;
            begin_time = ros::Time::now().toSec();
            data[0] = begin_time;
            data[1] = horizonAngle;
            data[2] = verticalAngle;
            msg.data.resize(3);
            msg.data[0] = data[0];
            msg.data[1] = data[1];
            msg.data[2] = data[2];
            pub.publish(msg);
            // msg1.data = verticalAngle ; 
            // msg2.data = horizonAngle;
            
            // pub1.publish(msg1);
            // pub2.publish(msg2);
            
        }
    }
    // void projectPointCloud1(){
    //     // range image projection
    //     float verticalAngle;
    //     size_t cloudSize; 
    //     PointType thisPoint;

    //     cloudSize = laserCloudIn->points.size();

    //     for (size_t i = 0; i < cloudSize; ++i){
            
    //         thisPoint.x = laserCloudIn->points[i].x;
    //         thisPoint.y = laserCloudIn->points[i].y;
    //         thisPoint.z = laserCloudIn->points[i].z;
            
    //         verticalAngle = atan2(thisPoint.z, sqrt(thisPoint.x * thisPoint.x + thisPoint.y * thisPoint.y)) * 180 / M_PI;
            
    //         msg1.data = verticalAngle;
    //         pub1.publish(msg1);
        
    //     }
    // }
};

int main(int argc, char** argv){

    ros::init(argc, argv, "lego_loam");
    
    test IP;

    ROS_INFO("\033[1;32m---->\033[0m TEST START.");
    ros::Rate rate(100);
    while (ros::ok())
    {
        ros::spinOnce();
        // std::thread loopthread(&test::projectPointCloud, &IP);
        // std::thread loopthread1(&test::projectPointCloud1, &IP);
        
        // loopthread.join();
        // loopthread1.join();     

        IP.projectPointCloud();
        rate.sleep();
    }
    ros::spin();
    return 0;
}
