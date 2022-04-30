import os

import json
import rospy
from kondo_webots.msg import servo_command 

ACTION_PATH = os.path.dirname(__file__) + "/../actions/"
SAMPLING_PERIOD = 32

## Maybe we should use path instead of action name
def load_action(action_name):
    "Loads action json file from ../action folder"
    try:
        json_file = open(ACTION_PATH + action_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Action '{action_name}' not found inside action folder")
        return None
    else:
        with json_file:
            action = json.loads(json_file.read())
            return action

def execute_action(servo_pub, action):
    "Executes desired action"
    timestep = SAMPLING_PERIOD * action["header"]["framestep"]
    joints = action["header"]["joints"]
    frames = action["frames"]

    msg = servo_command()
    msg.names = joints

    rate = rospy.Rate(1000 / (timestep))

    def send(frame):
        print(f"Sent {frame} to {joints}")
        msg.values = frame
        servo_pub.publish(msg)

    for frame in frames[:-1]:
        send(frame)
        rate.sleep()

    send(frames[-1])

if __name__ == "__main__":
    rospy.init_node('executor', anonymous=False)
    test_action = load_action("test_action.json")
    pub = rospy.Publisher('servo_control', servo_command, queue_size=10, latch=True)
    execute_action(pub, test_action)
