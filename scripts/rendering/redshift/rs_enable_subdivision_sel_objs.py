"""
rs_enable_subdivision_sel_objs.py
"""
import maya.cmds as cmds
sel_nodes = cmds.ls(sl=True)
for node in sel_nodes:
    shape = cmds.listRelatives(node)
    attrExist = cmds.attributeQuery('rsEnableSubdivision', node=shape[0], exists=True)
    if attrExist:
        cmds.setAttr(shape[0]+".rsEnableSubdivision", 1)