import maya.cmds as cmds
sel = cmds.ls(sl=True)
for i in sel:
	list = cmds.listConnections(i, c=True, d=True, s=False, scn=True)
	for l in list:
		print l