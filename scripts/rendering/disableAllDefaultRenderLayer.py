"""
disableAllDefaultRenderLayer.py

Disable all defaultRenderLayer from rendering. Useful when having references etc.
"""
import maya.cmds as cmds
all_nodes = cmds.ls()
for i in all_nodes:
    if "defaultRenderLayer" in i:
        cmds.setAttr(i+".renderable", 0)