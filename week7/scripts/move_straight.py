#!/usr/bin/python3

import rospy

import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist

# this is based on the Robotics Back-End: https://roboticsbackend.com/oop-with-ros-in-python/

class MoveStraight:
    def __init__(self):
        self.counter = 0
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.sleep( rospy.Duration.from_sec(0.5) )
    
if __name__ == '__main__':
    rospy.init_node('move_straight')
    n = MoveStraight()
    rate = rospy.Rate(10.0)

    t = Twist()
    t.linear.x = 1.0
    n.pub.publish(t)
    rospy.sleep( rospy.Duration.from_sec(1.0) )
    t.linear.x = 0.0
    n.pub.publish(t)
    rospy.sleep( rospy.Duration.from_sec(1.0) )