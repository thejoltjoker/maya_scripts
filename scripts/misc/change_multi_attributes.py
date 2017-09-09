"""
change_multi_attributes.py

change multiple attributes at once
"""
import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)

# VARIABLES
attribute = 'pointLock'
value = 1

if sel_nodes:
    shape_nodes = cmds.listRelatives(shapes=True)

    for shape in shape_nodes:

        cmds.setAttr('.'.join([shape, attribute]), value)