connectAttr -f KK_001_010_Anm:Face_Rig:PUPILSShapeDeformed.instObjGroups[0] shaders_v017_eyes_MTLSG.dagSetMembers[24]
import maya.cmds as cmds
sel_nodes = cmds.ls(dagObjects=True, objectsOnly=True, shapes=True, selection=True)

for node in sel_nodes:
    print node
    # cmds.connectAttr(node+'.instObjGroups', 'shaders_v017_eyes_MTLSG.dagSetMembers', na=True)



#     select -r PM_GoggleShapeDeformed ;
# connectAttr -f PM_GoggleShapeDeformed.instObjGroups[0] rsMaterial1SG.dagSetMembers[0];
# // Result: Connected PM_GoggleShapeDeformed.instObjGroups to rsMaterial1SG.dagSetMembers. //
# select -cl  ;
# disconnectAttr PM_GoggleShapeDeformed.instObjGroups[0] rsMaterial1SG.dagSetMembers[0];
# // Result: Disconnect PM_GoggleShapeDeformed.instObjGroups from rsMaterial1SG.dagSetMembers. //
# connectAttr -f PM_GoggleShapeDeformed.instObjGroups[0] rsMaterial1SG.dagSetMembers[1];
# // Result: Connected PM_GoggleShapeDeformed.instObjGroups to rsMaterial1SG.dagSetMembers. //