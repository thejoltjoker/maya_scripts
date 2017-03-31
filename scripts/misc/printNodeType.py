"""
printNodeType.py

print the node type of the selected node(s).
"""
import maya.cmds as cmds

sel = cmds.ls(sl=True)
for i in sel:
	n = cmds.nodeType(i)
	print n