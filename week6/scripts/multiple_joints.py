#!/usr/bin/python3
import rospy

import math
import tf2_ros
import geometry_msgs.msg
from sensor_msgs.msg import JointState

# this is based on the ROS tf2 tutorial: http://wiki.ros.org/tf2/Tutorials/Writing%20a%20tf2%20listener%20%28Python%29


if __name__ == '__main__':

    rospy.init_node('tf2_look_at_hand')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # set initial angle
    angle = 0

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():

        try:
            trans = tfBuffer.lookup_transform('Head', 'l_gripper', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        print("head_gripper: x: %f y: %f z: %f", trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z)
        print("head_gripper_yaw: %f"%math.atan2(trans.transform.translation.y,trans.transform.translation.x ))

        try:
            trans = tfBuffer.lookup_transform('torso', 'l_gripper', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        print("torso_gripper: x: %f y: %f z: %f", trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z)
        print("torso_gripper_yaw: %f"%math.atan2(trans.transform.translation.y,trans.transform.translation.x ))


        #comment this out once it gets noisy
        rate.sleep()