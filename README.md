# Assignment 3 - Research Track 1
---------------------------------
A robot in the Gazebo environment simulator that can be controlled in 3 ways from which the user can choose to either control it by specifying the target position coordinates, or through the keyboard keys or using the keyboard but with an obstacle avoidance algorithm to prevent collision.
## Installing and Running
---------------------------
This project simulation requires a ROS installation along with the Gazebo simulator.
After the project is installed or cloned, the workspace should be built by running the following command in the root of the workspace:
```
$ catkin_make
```
After a successful build process, the project can be run by the following steps in the command line in seperate terminals:

```
$ roscore
```
```
$ roslaunch final_assignment simulation_gmapping.launch
```
```
$ roslaunch final_assignment move_base.launch
```
```
$ roslaunch assignment3_rt1 UI.launch
```
## Project Infrastructure Flowchart
-----------------------------------
