import rospy
import rosservice
from webots_ros.srv  import set_int
from webots_ros.msg  import Float64Stamped
from sensor_msgs.msg import JointState

ROBOT_NAME = "beep_beep"
SAMPLING_PERIOD = 32


#TODO add opportunity to add sensors manually without parsing service list 
def getSensors():
	srv_list = rosservice.get_service_list()
	psensor_set = set()
	imu_set = set()
	
	for srv in srv_list:
		srv_name = srv.split("/")
		if srv_name[1] == ROBOT_NAME:
			
			if srv_name[2].split("_")[-1] == "sensor":
				psensor = "/".join(srv_name[:-1])
				psensor_set.add(psensor)

			if srv_name[2].split("_")[0] == "imu":
				imu = "/".join(srv_name[:-1])
				imu_set.add(imu)
	
	## HARDCODED
	psensor_set.remove("/" + ROBOT_NAME + "/battery_sensor")
	
	return psensor_set, imu_set


def startSensors(sensors):
	psensor_set, imu_set = sensors	
	for sensor in (psensor_set | imu_set):
		enable_sensor = rospy.ServiceProxy(sensor + "/enable", set_int)
		res = enable_sensor(SAMPLING_PERIOD)
		if not res.success: 
			print("Error: failed to start sensor", sensor)


class PositionSensor():
	
	def __init__(self, psensor_name):
		self.position = -1
		self.header = None
		
		self.input_topic  = psensor_name + "/value"
		
		self.sub = rospy.Subscriber(self.input_topic, Float64Stamped, self.input_callback)
		rospy.wait_for_message(self.input_topic, Float64Stamped)
		
		self.joint_name   = "_".join(psensor_name.split("/")[2].split("_")[:-1])
		self.output_topic = "/" + ROBOT_NAME + "/" + self.joint_name + "/joint_state" 
		self.pub = rospy.Publisher(self.output_topic, JointState, queue_size=10)	
		rospy.Timer(rospy.Duration(SAMPLING_PERIOD / 1000), self.output_callback)
		
	def input_callback(self, msg):
		self.header   = msg.header
		self.position = msg.data
		
	def output_callback(self, event=None):
		msg = JointState()
		msg.header = self.header
		msg.name = self.joint_name
		msg.position = [self.position]
		self.pub.publish(msg)


if __name__ == "__main__":
	
	rospy.init_node('sensors', anonymous=True)
	
	sensors = getSensors()
	startSensors(sensors)
	
	psensor_set, imu_set = sensors
	
	for psensor in psensor_set:
		PositionSensor(psensor)
		
	rospy.spin()
		
