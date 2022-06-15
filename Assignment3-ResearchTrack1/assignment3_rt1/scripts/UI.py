#! /usr/bin/env python3
import rospy
import os
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import *

def check_user_input(x):
   try:
        float(x)
        return True
   except:
        return False

def target_callback(x_coordinate,y_coordinate): # callback function for the target based case 1
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server() # waiting for the server connection
	target = MoveBaseGoal() # creating the target
	target.target_pose.header.frame_id = 'map'    # setting the target parameters
	target.target_pose.pose.orientation.w = 1
	target.target_pose.pose.position.x = x_coordinate
	target.target_pose.pose.position.y = y_coordinate
	client.send_goal(target) # sending the target position
	wait_threshold_time = client.wait_for_result(timeout=rospy.Duration(50.0)) # waiting to reach the result within a specified time
	if not wait_threshold_time:
		client.cancel_goal()
		rospy.loginfo("\nTime is out! Unreached target!")
		return -1
	else:
		rospy.loginfo("\nTarget reached successfully!")
		return 1
        
def first_case():
	print("\nCase I")
	print("------")
	while True:
		x_coordinate = input("Enter the x coordinate: ")
		y_coordinate = input("Enter the y coordinate: ")
		if (check_user_input(x_coordinate) and check_user_input(y_coordinate)):
			x_coordinate = float(x_coordinate)
			y_coordinate = float(y_coordinate)
			break
		else:
			print("Wrong input! Please make sure your X and Y inputs are numbers!")
	print("The robot will move to the desired target position: (",x_coordinate,",",y_coordinate,")")
	target_callback(x_coordinate,y_coordinate)

def second_case(): # activating the launch files to lunch the teleop twist to control the robot
	print("Case II")
	print("-------")
	os.system("roslaunch assignment3_rt1 case2.launch") # launching the correspondent launch file

def third_case():
	print("Case III")
	print("--------")
	os.system("roslaunch assignment3_rt1 case3.launch") # launching the correspondent launch file
 
def main():
	rospy.init_node('userInterface') # ROS node initialization
	while(1):
	# Terminal menu display for the user's choice
		print('''\nPlease choose one of the following options:
1: Choose the X and Y coordinates of a target position for the robot to reach
2: Drive the robot using the keyboard
3: Drive the robot using the keyboard while it avoids the obstacles
4: Quit the program \n''') 
		user_option = input("Choice:  ")
		if (user_option == '1'):
			first_case()
		elif (user_option == '2'):
			second_case()  
		elif (user_option == '3'):
			third_case()
		elif (user_option == '4'):
			break
		else:
			print("Wrong choice, please try again with the specified choices in the menu")

if __name__=="__main__":
	main()
