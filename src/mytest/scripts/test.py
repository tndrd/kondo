#!/usr/bin/env python

import rospy
from std_msgs.msg   import Float64, String
from webots_ros.srv import set_float

rospy.init_node('test', anonymous=True)

robot_name = rospy.wait_for_message('/model_name', String).data


head_yaw_vel_srv = '/' + robot_name + '/head_yaw/set_velocity'
 
rospy.wait_for_service(head_yaw_vel_srv)

try:
    head_rot_set_vel = rospy.ServiceProxy(head_yaw_vel_srv, set_float)
    res = head_rot_set_vel(4.0)
    print(res)

except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

rospy.spin()
