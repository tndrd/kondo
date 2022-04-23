import rospy
from control getSrvList, getRobotControlSet
from math import sin
from std_msgs.msg import String
from servo_module.msg import servos

rospy.init_node('example_servo_publisher', anonymous=True)
pub = rospy.Publisher('servo_cmds', servos, queue_size=10)

srv_list  = getSrvList()
ctrl_list = list(getRobotControlSet(srv_list))

msg = servos()

msg.names  = ctrl_list
msg.values = [1 for srv in ctrl_list] 

x = 0
STEP = 3.14 / 6

r = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(msg)
	x += STEP
	r.sleep()
