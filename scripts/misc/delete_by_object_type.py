import maya.cmds as cmds
sel = cmds.ls()
for i in sel:
    if 'Constraint' in cmds.objectType(i):
        cmds.delete(i)