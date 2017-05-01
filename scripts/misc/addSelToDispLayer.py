import maya.cmds as cmds

mySel = cmds.ls(sl=True)
layerSel = cmds.ls(type='displayLayer')
for i in layerSel:
	print i
cmds.editDisplayLayerMembers( 'displayLayer1', mySel)