import maya.cmds as cmds
import maya.mel as mel

sel = cmds.ls(sl=True, mat=True)

for id, mat in enumerate(sel):
    mel.eval('vray addAttributesFromGroup {0} vray_material_id 1;'.format(mat))
    mel.eval('vrayAddAttr {0} vrayMaterialId;'.format(mat))
    cmds.setAttr(('{0}.vrayMaterialId'.format(mat)), id)
