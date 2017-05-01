import maya.cmds as cmds
import maya.mel as mel

sel = cmds.ls(sl=True)
allObjs = cmds.ls()

for selObj in sel:

	if cmds.attributeQuery('vrayObjectID', node=selObj, ex=True) is True:
		print selObj,
		print cmds.getAttr(selObj+".vrayObjectID")