import rospy
from math import sin
from std_msgs.msg import String
from servo_module.msg import servos

rospy.init_node('example_servo_publisher', anonymous=True)
pub = rospy.Publisher('servo_cmds', servos, queue_size=10)

msg = servos()
msg.names = ['head_yaw', 'right_shoulder_pitch', 'left_shoulder_pitch']

x = 0
STEP = 3.14 / 6

r = rospy.Rate(1)

while not rospy.is_shutdown():
	msg.values = [sin(x), sin(x), sin(x)]
	pub.publish(msg)
	x += STEP
	r.sleep()
