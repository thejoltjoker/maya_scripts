import maya.cmds as cmds

selectedObjects = cmds.ls( selection=True )

for obj in selectedObjects:
	cmds.setAttr(obj+'.constraintMethod', 2)
	cmds.setAttr(obj+'.strength', .1)
	cmds.setAttr(obj+'.tangentStrength', .2)