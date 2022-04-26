import rospy
import rosservice
import message_filters as mf
from webots_ros.srv  import set_int
from webots_ros.msg  import Float64Stamped
from sensor_msgs.msg import JointState

ROBOT_NAME = "beep_beep"
SAMPLING_PERIOD = 32
JOINT_STATE_TOPIC = "/joint_state"

#TODO add opportunity to add sensors manually without parsing service list 

def psensor2joint(psensor):
	return "_".join(psensor.split("/")[2].split("_")[:-1])

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
	
	psensors = list(psensor_set)
	imus     = list(imu_set)
	
	return psensors, imus


def startSensors(sensors):
	psensors, imus = sensors	
	for sensor in (psensors + imus):
		enable_sensor = rospy.ServiceProxy(sensor + "/enable", set_int)
		res = enable_sensor(SAMPLING_PERIOD)
		if not res.success: 
			print("Error: failed to start sensor", sensor)


def publishJointState(psensors):
	
	joints = list(map(psensor2joint, psensors))
	
	subscribers = [mf.Subscriber(psensor + "/value", Float64Stamped) for psensor in psensors]
	js_publisher = rospy.Publisher(JOINT_STATE_TOPIC, JointState, queue_size = 10)
	
	## Needs to be tweaked
	queue_size = 10
	fps = 100.
	delay = 1 / fps * 0.5
	
	def joints_callback(*msgs):

		js = JointState()
		time = rospy.Time.now()
		
		js.header.stamp.secs  = time.secs
		js.header.stamp.nsecs = time.nsecs

		for msg, joint in zip(msgs, joints):
			js.name.append(joint)
			js.position.append(msg.data)

		js_publisher.publish(js)
	
	mfilter = mf.ApproximateTimeSynchronizer(subscribers, queue_size, delay)
	mfilter.registerCallback(joints_callback)
	


if __name__ == "__main__":
	
	rospy.init_node('sensors', anonymous=True)
	
	sensors = getSensors()
	startSensors(sensors)
	
	psensors, imus = sensors
	
	publishJointState(psensors)
		
	rospy.spin()
		
