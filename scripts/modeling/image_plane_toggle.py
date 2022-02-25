import maya.cmds as cmds

nodes = cmds.ls()

for node in nodes:
    if cmds.getAttr(node + '.displayMode') != 0:
        cmds.setAttr(node + '.displayMode', 0)
    elif cmds.getAttr(node + '.displayMode') == 0:
        cmds.setAttr(node + '.displayMode', 3)
