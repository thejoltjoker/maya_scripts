#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_control_offset.py
Description of create_control_offset.py.
"""
import maya.cmds as cmds


def set_attr():
    """docstring for main"""
    sel = cmds.ls(sl=True)

    attribute = 'offset'
    value = 0
    # shape = cmds.listRelatives(sel[1], shapes=True)[0]

    for node in sel:
        if cmds.attributeQuery('offset', node=node, ex=True):
            node_attr = '.'.join([node, attribute])
            cmds.setAttr(node_attr, value)

            print("{attr} was set to {val}".format(attr=node_attr, val=value))


if __name__ == '__main__':
    set_attr()
