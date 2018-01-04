#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
from scipy.linalg import block_diag

d1 = 0.0
d2 = 0.0
d3 = 0.0


def callback(msg):

	global d1
	global d2
	global d3

	d1 = msg.ranges[0]
    d2 = msg.ranges[719]
    d3 = (d1+d2)/2
    
	if (d1==d2):
	 move.linear.x=0.1
	elif (d2>d1):
	 move.angular.z=-pi/2        # turn right
	else:
     move.angular.z = pi/2       # turn left


	pub.publish(move)

rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/laser/scan',LaserScan,callback)
pub = rospy.Publisher('/cmd_vel',Twist)
move = Twist()

rospy.spin()
