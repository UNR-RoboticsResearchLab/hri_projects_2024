#!/usr/bin/python3

import rospy

import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler

# this is based on the Robotics Back-End: https://roboticsbackend.com/oop-with-ros-in-python/

class TurnOdom:
    def __init__(self):
        self.odom = Odometry()

        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.sub = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        rospy.sleep( rospy.Duration.from_sec(0.5) )

    def odom_callback(self, msg):
        self.odom = msg

    def get_yaw (self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        return yaw

    def get_odom(self):
        return self.odom

if __name__ == '__main__':
    rospy.init_node('move_straight')
    n = TurnOdom()
    rate = rospy.Rate(15.0)


    # figure out where we started from
    start = n.get_yaw(n.get_odom())

    # start the robot's movement
    t = Twist()
    t.angular.z = 0.5
    n.pub.publish(t)

    while not rospy.is_shutdown():

        # maintain current rate
        n.pub.publish(t)

        # get current odom
        cur = n.get_yaw(n.get_odom())

        # is distance greater than 1 rad?
        # distance
        arcdist = math.fabs(cur - start)
        print(arcdist)

        if arcdist > 1.0:
            t.angular.z = 0.0
            n.pub.publish(t)
            break

        rate.sleep()

    t.angular.z = 0.0
    n.pub.publish(t)
    rospy.sleep( rospy.Duration.from_sec(1.0) )