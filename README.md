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
![Flowchart](https://user-images.githubusercontent.com/79665691/173406444-8c001c0b-0036-43c0-afdd-8c9a5381d817.png)

As shown in the above flowchart, the UI.launch file will launch the user interface script which will ask the user for his choice, where he can choose the first case to set a target position which will trigger a callback function in the same script to achieve the goal of this case. Moreover, the user can choose the second or third case which will launch another launch file correspondent to the chosen case, which by itself will run the required nodes. Furthermore, the user can choose to quit the program by entering 4 as input.
