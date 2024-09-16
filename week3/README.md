# Week 3 Tutorial

This week we're going to start actually moving the 'simulation' of the Nao robot and start playing around with some code.

## Starting up our humanoid 'simulation'

(from last week)

- Rather than running a full nao simulator, we're going to just play with a model nao in rviz. Let's start with loading a description of the nao into ROS:

```
roslaunch week2 nao_sim.launch
```

- In another terminal, start up an instance of `rviz`, add a RobotModel.

```
rosrun rviz rviz
```

## Moving one joint on the Nao

To start this week, let's check out the joint_demo.py, that I've included in your week3 directory:

```
rosrun week3 joint_demo.py
```

This will start moving the nao's head in an admittedly freaky way.

Let's check out how this works!

### The joint_states message

`rosmsg show sensor_msgs/JointState` should show the message type for the message we'll be using:

```
sensor_msgs/JointState 
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string[] name
float64[] position
float64[] velocity
float64[] effort
```