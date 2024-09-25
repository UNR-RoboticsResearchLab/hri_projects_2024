# Week 3 Tutorial

This week we're going to continue moving the 'simulation' of the Nao robot but now add a new library (TF2) that will help us move the robot pretty intelligently.

*** Note: the TF2 library is really well-documented here: http://wiki.ros.org/tf2

## Let's look at the script tf_look_at_hand.py:

First off, in several terminals, start the `nao_sim.launch`, the `joint_state_publisher_gui`, and `rviz` to visualize our Nao.

Next, let's run this node, `scripts/tf_look_at_hand.py` to see what it is doing:

```
#!/usr/bin/python3
import rospy

import math
import tf2_ros
import geometry_msgs.msg

# this is based on the ROS tf2 tutorial: http://wiki.ros.org/tf2/Tutorials/Writing%20a%20tf2%20listener%20%28Python%29

if __name__ == '__main__':
    rospy.init_node('tf2_look_at_hand')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)


    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('Head', 'LFinger23_link', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        print("trans: x: %f y: %f z: %f", trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z)
        rate.sleep()
```

## Goals for this/next week

1. Look at the hand as it moves to any position
2. Write a node that uses the head/eyes to gesture toward the hand
3. Write another node that keeps the head pointed at the hand
4. Write a final node that look in the direction that the hand is pointing

The above, plus the week3 deliverables will consitute our first larger project, due Oct 04, 2024.