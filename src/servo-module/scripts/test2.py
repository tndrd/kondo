#!/usr/bin/env python

import rospy
import asyncio
import rosservice
from time import time
from std_msgs.msg   import Float64, String
from webots_ros.srv import set_float

ROBOT_NAME = "beep_beep"
#robot_name = rospy.wait_for_message('/model_name', String).data

rospy.init_node('test', anonymous=True)
print('hehe')

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
			print(srv_name)
			client = rospy.ServiceProxy(srv_name, set_float)
			servo_dict[ctrl_unit] = client
		else:
			print("Trying to register proxy of service %s, which is not available")
	
	return servo_dict, ctrl_set

def sendCommandsAsync(servo_dict, name_list, val_list):
	
	assert len(name_list) == len(val_list)
	
	async def exec_cmd(name, val):
		print("Rotating %s..." % name)
		await servo_dict[name](val) 
		print("Finished %s..." % name)
		
	ioloop = asyncio.get_event_loop()
	tasks = []
	
	for name, val in zip(name_list, val_list):	
		if name not in servo_dict:
			print("Wrong command: servo %s is not available" % name)
			continue
		task = ioloop.create_task(exec_cmd(name, val))
		tasks.append(task)
	
	wait_tasks = asyncio.wait(tasks)
	ioloop.run_until_complete(wait_tasks)
	ioloop.close() 
	
	#print("Done!")
			
def sendCommandsSync(servo_dict, name_list, val_list):
	
	assert len(name_list) == len(val_list)
	
	for name, val in zip(name_list, val_list):	
		if name not in servo_dict:
			print("Wrong command: servo %s is not available" % name)
			continue
		#print("Rotating %s..." % name)
		servo_dict[name](val)
	#print("Done!")


		
'''
async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

'''

servo_dict, ctrl_set = registerServoDict()

name_list = list(ctrl_set)
val_list  = [1 for name in name_list]

print("Async call:")
start = time()
sendCommandsAsync(servo_dict, name_list, val_list)
elapsed = time() - start
print("Done in %s s" % elapsed)

print("Sync call:")
start = time()
sendCommandsSync(servo_dict, name_list, val_list)
elapsed = time() - start
print("Done in %s s" % elapsed)
'''
head_yaw_srv = '/' + robot_name + '/head_yaw/set_position'
 
rospy.wait_for_service(head_yaw_srv)

try:
    head_rot = rospy.ServiceProxy(head_yaw_srv, set_float)
    res = head_rot(0.5)
    print(res)

except rospy.ServiceException as e:
    print("Service call failed: %s"%e)
'''


