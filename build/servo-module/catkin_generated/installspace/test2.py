#!/usr/bin/env python3

import rospy
from std_msgs.msg   import Float64, String
from webots_ros.srv import set_float

rospy.init_node('test', anonymous=True)
print('hehe')

'''
#robot_name = rospy.wait_for_message('/model_name', String).data
robot_name="beep_beep"

head_yaw_srv = '/' + robot_name + '/head_yaw/set_position'
 
rospy.wait_for_service(head_yaw_srv)

try:
    head_rot = rospy.ServiceProxy(head_yaw_srv, set_float)
    res = head_rot(0.5)
    print(res)

except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

rospy.spin()
'''
