import json
import rospy

ACTION_PATH = "../actions/"

act_file = open(ACTION_PATH + "test_action.json", "r").read()
print(act_file) 

