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
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string[] name
float64[] position
float64[] velocity
float64[] effort
```

We can ignore the `velocity` and `effort` fields for now. Let's start with:

```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
```

This is a header, a message made up of more messages. The header has three parts (helfully indented for easy reading). The 'seq' field helps order messages, the `stamp` field is the ROSTIME, an the 'frame_id' field, says what frame of reference these are in. Let's set the time and the frame.

Next let's look at the two fields relevant for our work this week:

```
string[] name
float64[] position
```

These are both lists (hence the '[]' at the end of the type). These lists should be equal length, the 'name' is the name of the joint to set, and the 'position' is what position (in radians) to set it to.

We can set those joint names and positions as follows:

```
        # put in some joints that we'll edit
        js.name.append("HeadYaw")
        js.name.append("HeadPitch")

        js.position.append(math.radians(angle))
        js.position.append(0)
```

*** Note: this doesn't actually change the joints!! That doesn't happen until we send the message:

```
        pub.publish(joint_states)
```

## What to complete for this week

Let's start moving joints:

* Add a complete list of joints to the joint_states message
* Edit my script to work as a sequence of actions, rather than a loop
** make sure to have delays between changes of position
* Create a simple animation with a set of poses
** wave hi
** nod head
** shake head
* Reach: make interpolated actions, rather than just setting individual frames

