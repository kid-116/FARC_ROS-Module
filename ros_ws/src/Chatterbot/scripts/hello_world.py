#!/usr/bin/env python

import rospy

def main():    
    # Make the script a ROS Node
    rospy.init_node('node_hello_ros', anonymous=True)

    # Print info on console
    rospy.loginfo("Hello world!")
    
    # Keep the node unless killed by user
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass