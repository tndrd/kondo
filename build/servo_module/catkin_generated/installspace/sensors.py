import rospy
import rosservice

ROBOT_NAME = "beep_beep"



def getPositionSensors():
	srv_list = rosservice.get_service_list()
	psensor_set = set()
	
	for srv in srv_list:
		srv_name = srv.split()
		if srv_name[1] == "ROBOT_NAME" and srv_name[2].split("_")[-1] == "sensor":
			psensor = "/".join(srv_name[:-1])
			psensor_set.add(psensor)
	print(psensor_set)
	
getPosititonSensors()
		
