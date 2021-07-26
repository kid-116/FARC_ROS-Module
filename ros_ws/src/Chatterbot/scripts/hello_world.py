#!/usr/bin/env python

import rospy

def main():
    # Making the script a ROS Node
    rospy.init_node('node_hello_ros', anonymous=True)

    # Print info on console
    rospy.loginfo("Hello world!")

    # Keep the node alive unless killed by user
    # rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInternalException:
        pass