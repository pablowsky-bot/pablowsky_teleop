#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

linear_scale = 0.5
angular_scale = 3.5

cmd_vel_msg = Twist()

cmd_vel_msg.linear.x = 0.0
cmd_vel_msg.linear.y = 0.0
cmd_vel_msg.linear.z = 0.0

cmd_vel_msg.angular.x = 0.0
cmd_vel_msg.angular.y = 0.0
cmd_vel_msg.angular.z = 0.0

def callback(msg):
    cmd_vel_msg.linear.x = msg.axes[1] * linear_scale
    cmd_vel_msg.angular.z = msg.axes[3] * angular_scale

def gamepad_teleop():
    rospy.init_node('gamepad_teleop', anonymous=True)
    rospy.loginfo('pablowsky gamepad teleop node started')
    rospy.Subscriber("joy", Joy, callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(cmd_vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        gamepad_teleop()
    except rospy.ROSInterruptException:
        pass
