import maya.cmds as cmds
# mens = cmds.select('set*', noExpand=True)
objectSetsList = cmds.ls( 'set*', type='objectSet' )
for i in objectSetsList:
	
	if cmds.objectType(i, isType='objectSet'):
		cmds.delete(i)