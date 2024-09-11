# Week 2 Tutorial

This week we're going to start with some ROS command-line things and then move on to playing with the nao.

## Install nao packages

So, they stopped packaging the nao

```
sudo apt install ros-noetic-naoqi-driver ros-noetic-move-base-msgs ros-noetic-nao-meshes
cd ~/hri2024/src
git clone git@github.com:ros-naoqi/nao_robot.git
cd ..
catkin_make
```

*Note: if you don't have a package version of ros-noetic-nao-meshes, you can clone it into your workspace, `git clone https://github.com/ros-naoqi/nao_meshes/`*

This will add the nao packages to your workspace and compile them.

make sure to come back to the week2 directory:

```
roscd week2
```

*we'll pick up the nao simulation stuff in a minute, but first we need to play a bit with some ROS command line commands*

## Command-Line fun

let's start by opening up three terminals, (make sure to run the `source ~/hri2024/devel/setup.bash` command to set up the ROS stuff)

in the first terminal, run the roscore node:

```
roscore
```

in the second terminal, run the talker node:

```
rosrun week0 talker
```

let that guy run, it'll do its job. But let's see what info we can learn in our third terminal. Let's start with the rosnode command:

```
rosnode list
```

you should see two nodes running, something like:

/rosout
/talker_17741_1726030205396

you can then use the same command to get info about a node if you want:

```
rosnode info <node name>
```

that gave me some info like this:

--------------------------------------------------------------------------------
Node [/talker_17741_1726030205396]
Publications: 
 * /chatter [std_msgs/String]
 * /rosout [rosgraph_msgs/Log]

Subscriptions: None

Services: 
 * /talker_17741_1726030205396/get_loggers
 * /talker_17741_1726030205396/set_logger_level


contacting node http://metatron:43323/ ...
Pid: 17741
Connections:
 * topic: /rosout
    * to: /rosout
    * direction: outbound (32769 - 127.0.0.1:42130) [9]
    * transport: TCPROS
