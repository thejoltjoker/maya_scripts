"""listFileNodesWithSpaces.py

This script prints the name and selects every file node with a space in the filename.
"""
import maya.cmds as cmds

allTextures = cmds.ls()
cmds.select(d=True)

for texture in allTextures:
    if cmds.nodeType(texture) == 'file':
        texturePath = cmds.getAttr(texture+'.fileTextureName')
        if ' ' in texturePath:
            print texture+' has a space in the path '+texturePath
            cmds.select(texture, add=True)