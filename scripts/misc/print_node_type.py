"""
printNodeType.py

print the node type of the selected node(s).
"""
import maya.cmds as cmds


def main():
    sel = cmds.ls(sl=True)
    for i in sel:
        n = cmds.nodeType(i)
        cmds.warning('NodeType: ' + n)
