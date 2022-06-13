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

As shown in the above flowchart, the UI.launch file will launch the user interface script which will ask the user for his choice, where he can choose the first case to set a target position which will trigger a callback function in the same script to achieve the goal of this case. This function will ask the user to enter the X and Y coordinates of the desired goal for the robot to reach, then this position will be sent to the simulator. 
Moreover, the user can choose the second case where a specific launch file will be launched to run the correspondent teleop node enabling the user to control the robot using the keyboard. Additionally when the user chooses the third case, another launch file will be launched to run the same teleop node along with an obstacle avoider node enabling the user to control the robot via keyboard while avoiding obstacles. Furthermore, the user can choose to quit the program by entering 4 as input.

## Obstacle Avoider Flowchart
-----------------------------
![AvoiderFlowchart](https://user-images.githubusercontent.com/79665691/173417605-eb8755bd-946c-4438-aedf-a041836bf99d.png)

As shown in the obstacle avoider flowchart above, the program divides the obstacle information into three main directions, Front, Front Left and Front Right. The robot will first check if there is any obstacle closer than the predefined distance condition which will lead to stop its motion in the linear direction. However, if there is no close obstacle in the front direction, the robot will check the Front Left and Front Right obstacles, which if were less than the distance threshold, the robot angular motion will be stopped. Moreover, if no close obstacles were detected in any of the 3 main directions, the robot can still be controlled to move in any direction without the need to go backwards.

## Project Possible Improvements
--------------------------------
Instead of Laserscan, the camera plugin in the Gazebo simulator can be used to simulate robots' camera functionalities such as depth, which provides the robot with greater insight about its surrounding environment and obstacles. For instance, the kinect camera can be simulated with the objective to improve the obstacle avoidance feature and increase the mapping efficiency of the environment, and thus, making the robot more robust and adaptive to any change that might occur in the environment. For this purpose, Openni Kinect can be used as it also publishes the same topics as the corresponding ROS drivers for the Microsoft Kinect which are specified in the [documentation](https://wiki.ros.org/openni_camera).
