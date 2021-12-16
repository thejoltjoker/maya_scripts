import maya.cmds as cmds

selectedObjs = cmds.ls(sl=True)

for obj in selectedObjs:

    shapes = cmds.listRelatives(obj, c=True, ad=True)

    cmds.connectAttr(obj+'.offset', shapes[1]+'.visibility')
