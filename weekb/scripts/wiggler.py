#!/usr/bin/python3
# license removed for brevity

import rospy
import random
from geometry_msgs.msg import Twist

def get_random_cmd_vel() -> Twist:
    xvel = random.gauss(0, 0.3)
    yvel = random.gauss(0, 0.2)
    turn = random.gauss(0, 0.2)
    cmd_vel = Twist()

    cmd_vel.linear.x = xvel
    cmd_vel.linear.y = yvel
    cmd_vel.angular.z = turn

    return cmd_vel




def wiggler():
    pub_1 = rospy.Publisher('/robot_1/cmd_vel', Twist, queue_size=10)
    pub_2 = rospy.Publisher('/robot_2/cmd_vel', Twist, queue_size=10)
    pub_3 = rospy.Publisher('/robot_3/cmd_vel', Twist, queue_size=10)
    rospy.init_node('wiggler', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    random.seed()
    while not rospy.is_shutdown():
        # generate random x and y values
        # xvel_1 = random.gauss(0, 0.3)
        # yvel_1 = random.gauss(0, 0.2)
        # turn_1 = random.gauss(0, 0.2)
        # cmd_vel = Twist()
        # cmd_vel.linear.x = xvel
        # cmd_vel.linear.y = yvel
        # cmd_vel.angular.z = turn

        pub_1.publish(get_random_cmd_vel())
        pub_2.publish(get_random_cmd_vel())
        pub_3.publish(get_random_cmd_vel())
        rate.sleep()

if __name__ == '__main__':
    try:
        wiggler()
    except rospy.ROSInterruptException:
        pass