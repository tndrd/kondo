#!/usr/bin/env python

import rospy
import threading
import rosservice

from time import time
from std_msgs.msg     import Float64, String
from webots_ros.srv   import set_float
from servo_module.msg import servos


ROBOT_NAME = "beep_beep"
#robot_name = rospy.wait_for_message('/model_name', String).data

def getSrvList():
	srv_list = rosservice.get_service_list()
	return srv_list

def ctrl2srv(ctrl):
	return '/' + ROBOT_NAME + '/' + ctrl + '/set_position'
	
# servo name set should be created manually if it is possible to avoid wrong entity calls
def getRobotControlSet(srv_list):
	ctrl_set = set()
	for srv in srv_list:
		srv = srv.split("/")
		if srv[1] == ROBOT_NAME:
			ctrl_unit = srv[2]
			ctrl_set.add(ctrl_unit)
	
	ctrl_set = cleanControlSet(ctrl_set)
	return ctrl_set


def cleanControlSet(ctrl_set):
	clean_ctrl_set = set()
	srv_list = getSrvList()
	
	for ctrl_unit in ctrl_set:
		srv_name = ctrl2srv(ctrl_unit)
		if srv_name in srv_list:
			clean_ctrl_set.add(ctrl_unit)
	return clean_ctrl_set

		
def registerServoDict(ctrl_set = None):
	
	servo_dict = dict()
	srv_list = getSrvList()
	
	if ctrl_set is None:
		ctrl_set = getRobotControlSet(srv_list)
	
	for ctrl_unit in ctrl_set:
		srv_name = ctrl2srv(ctrl_unit)
		if srv_name in srv_list:
			client = rospy.ServiceProxy(srv_name, set_float)
			servo_dict[ctrl_unit] = client
		else:
			print("Trying to register proxy of service %s, which is not available")
	
	return servo_dict, ctrl_set
	

def sendCommands(servo_dict, name_list, val_list):
	
	assert len(name_list) == len(val_list)
	
	def exec_cmd(name, val):
		srv_name = ctrl2srv(name)
		rospy.wait_for_service(srv_name)
		servo_dict[name](val)
	
	for name, val in zip(name_list, val_list):	
		if name not in servo_dict:
			print("Wrong command: servo %s is not available" % name)
			continue
		proxy_thread = threading.Thread(target=exec_cmd, args=(name, val))
		proxy_thread.start()
	
if __name__ == "__main__":
	rospy.init_node('servo_cmds', anonymous=True)

	servo_dict, ctrl_set = registerServoDict()
	
	def servosCallback(msg):
		print("Recieved: ", msg.names, msg.values)
		start = time()
		
		### Used for performance test
		#names = list(ctrl_set)
		#values = [1 for name in names]
		#sendCommands(servo_dict, names, values)
		
		sendCommands(servo_dict, msg.names, msg.values)
		print("Processed in %s ms\n" % ((time() - start) * 1000))
		
	rospy.Subscriber("servo_cmds", servos, servosCallback)
	print("Listening to commands...")
	rospy.spin()
























	
	
	
