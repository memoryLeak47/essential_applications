#!/usr/bin/env python3

import os

def getConfigFilePath():
	return os.path.expanduser("~") + "/.ul-config"

def getULRoot():
	print("nop")
	
def setULRoot(root):
	print("ULRoot set to: " + root)
	config = open(getConfigFilePath())
	lines = config.readlines()
	lines[0] = root
	config.close()
	config = open(getConfigFilePath(), "w")
	config.writelines(lines)
	config.close()
	
