#!/usr/bin/python3.4 -B

import os

def getConfigFilePath():
	return os.path.expanduser("~") + "/.ul-config"

def getULRoot():
	config = open(getConfigFilePath())
	line = config.readlines()[0]
	config.close()
	return line
	
def setULRoot(root):
	print("ULRoot set to: " + root)
	if os.path.isfile(getConfigFilePath()):
		config = open(getConfigFilePath())
		lines = config.readlines()
		if len(lines) != 0:
			lines[0] = root + "\n"
		else:
			lines.append(root + "\n")
		config.close()
		config = open(getConfigFilePath(), "w")
		config.writelines(lines)
		config.close()
	else:
		config = open(getConfigFilePath(), "w")
		config.writelines(root + "\n")
		config.close()
	
