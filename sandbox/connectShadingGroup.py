connectAttr -f KK_001_010_Anm:Face_Rig:PUPILSShapeDeformed.instObjGroups[0] shaders_v017_eyes_MTLSG.dagSetMembers[24]
import maya.cmds as cmds
sel_nodes = cmds.ls(dagObjects=True, objectsOnly=True, shapes=True, selection=True)

for node in sel_nodes:
    print node
    # cmds.connectAttr(node+'.instObjGroups', 'shaders_v017_eyes_MTLSG.dagSetMembers', na=True)