from xml.dom import minidom

DATA_PATH = "../launch/init.launch"

data = open(DATA_PATH, "r").read()

dom = minidom.parseString(data)
dom.normalize()
print(dom)
