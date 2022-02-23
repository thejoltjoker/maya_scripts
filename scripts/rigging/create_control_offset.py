#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_control_offset.py
Description of create_control_offset.py.
"""
import maya.cmds as cmds
import maya.mel as mel


def create_curve_hexagon():
    mel.eval(
        'curve -d 1 -p -0.5 0.25 -0.866026 -p 0.5 0.25 -0.866025 -p 1 0.25 0 -p 0.5 0.25 0.866025 -p -0.5 0.25 0.866025 -p -1 0.25 -1.49012e-07 -p -0.5 0.25 -0.866026 -p -0.5 -0.25 -0.866026 -p 0.5 -0.25 -0.866025 -p 1 -0.25 0 -p 0.5 -0.25 0.866025 -p -0.5 -0.25 0.866025 -p -1 -0.25 -1.49012e-07 -p -0.5 -0.25 -0.866026 -p -0.5 0.25 -0.866026 -p 0.5 0.25 -0.866025 -p 0.5 -0.25 -0.866025 -p 1 -0.25 0 -p 1 0.25 0 -p 0.5 0.25 0.866025 -p 0.5 -0.25 0.866025 -p -0.5 -0.25 0.866025 -p -0.5 0.25 0.866025 -p -1 0.25 -1.49012e-07 -p -1 -0.25 -1.49012e-07 -p -0.5 -0.25 -0.866026 -p -0.5 0.25 -0.866026 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 ;')


def create_curve_cube():
    # curve -d 1 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;
    #     curve -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;
    cube = cmds.curve(d=1, p=[(1, 1, 1), (-1, 1, 1), (-1, 1, -1), (1, 1, -1), (-1, -1, -1), (1, -1, -1), (-1, -1, 1)])


def connect_offset_visibility():
    """
    First select controller, then offset
    """
    sel = cmds.ls(sl=True)
    control = sel[0]
    offset_shape = cmds.listRelatives(sel[1], shapes=True)[0]

    if not cmds.attributeQuery('offset', node=control, ex=True):
        cmds.select(control)
        cmds.addAttr(ln="offset", at='bool', k=True)

    cmds.connectAttr('{}.offset'.format(control),
                     '{}.visibility'.format(offset_shape))


if __name__ == '__main__':
    connect_offset_visibility()