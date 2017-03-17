"""
renameFileNodeToFilename.py

Rename file nodes in maya to be the name of the input file.
"""
import os
import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)

for node in sel_nodes:
    if cmds.nodeType(node) == 'file':
        texturePath = cmds.getAttr(node+".fileTextureName")
        filenameExt = os.path.basename(texturePath)
        filename = os.path.splitext(filenameExt)[0]
        cmds.rename(node, filename)
