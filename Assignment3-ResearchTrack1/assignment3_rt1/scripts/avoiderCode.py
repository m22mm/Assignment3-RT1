#! /usr/bin/env python3
import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

distance_precondition = 0.7 # distance threshold
init = Vector3(0, 0, 0)
velocity = Twist(init, init)

def callback_function(info): # Receiving the robot's linear and angular velocities 
	global velocity
	velocity = info

def receive_dist(info): # The robot receives the obstacle info from the cmd_vel topic
	global velocity
	publisher = rospy.Publisher('cmd_vel',Twist, queue_size=10)
	# obstacles' distance ranges computation
	directions = { 
		'frontRight_obstacle': min(min(info.ranges[144:287]), 10),
		'front_obstacle':  min(min(info.ranges[288:431]), 10),
		'frontleft_obstacle':  min(min(info.ranges[432:575]), 10),
	}
	if directions['front_obstacle'] < distance_precondition:
		velocity.linear.x = 0 # null linear velocity when front obstacle detected in less than 0.7 distance
        
	elif directions['frontleft_obstacle'] < distance_precondition or directions['frontRight_obstacle'] < distance_precondition:
		velocity.angular.z = 0 # null angular velocity when front left or front right obstacles detected in less than 0.7 distance

	publisher.publish(velocity) # publishing on the "cmd_vel" topic

def main():
	rospy.init_node('obstacle_avoider') # node initialization
	rospy.Subscriber('/remap_cmd_vel', Twist, callback_function) # subscription to the topic "remap_cmd_vel"    
	rospy.Subscriber('/scan', LaserScan, receive_dist) # subscription to the topic "scan"
	rospy.spin()

if __name__ == '__main__':
	main()
