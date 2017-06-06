"""
center_pivot_world.py

Centers the pivor of selected objects to world 0, 0, 0.
"""
import maya.cmds as cmds

sel = cmds.ls(sl=True)
for i in sel:
    cmds.xform(piv=(0, 0, 0))
