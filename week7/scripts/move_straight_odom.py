#!/usr/bin/python3

import rospy

import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# this is based on the Robotics Back-End: https://roboticsbackend.com/oop-with-ros-in-python/

class MoveStraightOdom:
    def __init__(self):
        self.odom = Odometry()

        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.sub = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        rospy.sleep( rospy.Duration.from_sec(0.5) )

    def odom_callback(self, msg):
        self.odom = msg

    def get_odom(self):
        return self.odom

if __name__ == '__main__':
    rospy.init_node('move_straight')
    n = MoveStraightOdom()
    rate = rospy.Rate(15.0)


    # figure out where we started from
    start = n.get_odom()

    # start the robot's movement
    t = Twist()
    t.linear.x = 1.0
    n.pub.publish(t)

    while not rospy.is_shutdown():

        # maintain current rate
        n.pub.publish(t)

        # get current odom
        cur = n.get_odom()

        # is distance greater than 1m?
        dx = cur.pose.pose.position.x - start.pose.pose.position.x
        dy = cur.pose.pose.position.y - start.pose.pose.position.y

        # distance
        dist = math.sqrt( dx*dx + dy*dy )
        print(dist)

        if dist > 1.0:
            t.linear.x = 0.0
            n.pub.publish(t)
            break

        rate.sleep()

    t.linear.x = 0.0
    n.pub.publish(t)
    rospy.sleep( rospy.Duration.from_sec(1.0) )