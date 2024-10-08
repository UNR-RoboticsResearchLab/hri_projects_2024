#!/usr/bin/python3

import rospy

import math
import tf2_ros
import geometry_msgs.msg
from std_msgs.msg import Int64

# this is based on the Robotics Back-End: https://roboticsbackend.com/oop-with-ros-in-python/

class NumberCounter:
    def __init__(self):
        self.counter = 0
        self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)
        self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_number)
        self.msg = Int64()

    def callback_number(self, msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.msg = new_msg
        #self.pub.publish(new_msg)

    def get_msg(self):
    	return self.msg

if __name__ == '__main__':
    rospy.init_node('number_counter')
    n = NumberCounter()
    #rospy.spin()
    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
    	n.pub.publish(n.get_msg())
    	rate.sleep()
