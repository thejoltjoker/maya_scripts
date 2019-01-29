import maya.cmds as cmds

def mayaSublimePort():
	# if it was already open under another configuration
	cmds.commandPort(name=":7002", close=True)

	# now open a new port
	cmds.commandPort(name=":7002", sourceType="python")

	# or open some random MEL port (make sure you change it to this port in your config file)
	cmds.commandPort(name=":10000", sourceType="mel")

mayaSublimePort()
