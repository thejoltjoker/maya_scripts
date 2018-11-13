#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
assign_to_sg.py
Description of assign_to_sg.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    shapes = [x for x in cmds.ls(sl=True) if cmds.nodeType(x) == 'mesh']
    shading_group = cmds.ls(sl=True)[-1]
    for obj in shapes:
        cmds.sets(obj, e=True, forceElement=shading_group)


if __name__ == '__main__':
    main()

# for i in cmds.listRelatives('StormTrooperSWC_Rig4_StormTrooperSWC_Model:calf_L_geo', pa=True):
#     print [x for x in cmds.listConnections(i, p=1) if cmds.nodeType(x) == 'shadingEngine']