# Week 2 Tutorial

This week we're going to start with some ROS command-line things and then move on to .

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
