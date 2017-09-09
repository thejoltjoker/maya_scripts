"""
rename_file_node_to_filename.py

Rename file nodes in maya to be the name of the input file.
"""
import os
import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)

for node in sel_nodes:
    if cmds.nodeType(node) == 'shadingEngine':
        surface_shader_name = cmds.getAttr(node+".surfaceShader")
        print surface_shader_name
        filename = surface_shader_name+'_SG'
        cmds.rename(node, filename)
