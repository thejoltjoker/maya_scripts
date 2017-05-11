"""
cam_loc_scale.py
"""
import maya.cmds as cmds

sel = cmds.ls( selection=True)
for i in sel:
    cam = cmds.listRelatives(shapes=True)

    for c in cam:
        curVal = cmds.getAttr(c+'.locatorScale')
        newVal = curVal * 1.25
        print newVal
        cmds.setAttr(c+'.locatorScale', newVal)