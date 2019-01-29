import maya.cmds as cmds

mySel = cmds.ls(sl=True)
sep = '_'
firstBorn = mySel[0].split(sep, 1)[0]
newGroupName = firstBorn+'_grp'
mirrorGroupName = firstBorn+'Mirrored_grp'

cmds.group( em=True, n=newGroupName)
objParent = cmds.listRelatives(mySel[0], p=True)
print objParent
cmds.parent(newGroupName, objParent)
for obj in mySel:
    cmds.parent(obj, newGroupName)

cmds.duplicate(newGroupName, n=firstBorn+'Mirrored_grp')
cmds.setAttr(mirrorGroupName+'.scaleX', -1);