#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_control_offset.py
Description of create_control_offset.py.
"""
import maya.cmds as cmds


def connect_offset_visibility():
    """docstring for main"""
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
