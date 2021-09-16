#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def circle():
    rospy.init_node('circle_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velocity = Twist()
    rate = rospy.Rate(10) #10Hz
    rospy.loginfo("moving the bot")
    radius = 3
    vel = 2
    alpha = 10**(-2) / radius * 3

    while not rospy.is_shutdown():
        velocity.linear.x = vel
        velocity.angular.z = vel / radius
        pub.publish(velocity)
        rate.sleep()
        if radius > 0:
            radius = (1 - alpha) * radius


    velocity.linear.x = 0
    velocity.angular.z = 0
    pub.publish(velocity)

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInternalException:
        pass