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
	config = open(getConfigFilePath())
	lines = config.readlines()
	lines[0] = root
	config.close()
	config = open(getConfigFilePath(), "w")
	config.writelines(lines)
	config.close()
	
