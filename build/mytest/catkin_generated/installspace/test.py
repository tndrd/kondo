#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

import controller
print(dir(controller))

from controller import Robot


print("hehe")

robot = Robot()
timeStep = int(robot.getBasicTimeStep())

head_yaw = robot.getDevice('head_yaw')

head_yaw.setPosition(float('inf'))

velocity = 1

head_yaw.setVelocity(velocity)

while robot.step(timeStep) != -1 and not rospy.is_shutdown():
    rospy.spinOnce()
