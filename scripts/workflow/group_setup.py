#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
group_setup.py
Create a basic scene structure with groups
"""
import maya.cmds as cmds


def add_suffix(name, suffix, sep='_'):
    return sep.join([name, suffix])


def create_groups(parent, groups, suffix='grp', sep='_', suffix_uppercase=False):
    """docstring for main"""
    suffix = 'grp'
    if suffix_uppercase:
        suffix = suffix.upper()

    # Create parent group
    parent = add_suffix(parent, suffix, sep)
    cmds.group(em=True, name=parent)

    # create groups
    for g in groups:
        cmds.group(em=True, name=add_suffix(g, suffix, sep))
        cmds.parent(g, parent)

    groups.append(parent)

    # lock group attributes
    for l in groups:
        cmds.setAttr(l + '.translateX', lock=True)
        cmds.setAttr(l + '.translateY', lock=True)
        cmds.setAttr(l + '.translateZ', lock=True)
        cmds.setAttr(l + '.scaleX', lock=True)
        cmds.setAttr(l + '.scaleY', lock=True)
        cmds.setAttr(l + '.scaleZ', lock=True)
        cmds.setAttr(l + '.rotateX', lock=True)
        cmds.setAttr(l + '.rotateY', lock=True)
        cmds.setAttr(l + '.rotateZ', lock=True)


if __name__ == '__main__':
    create_groups('scene', ['geo', 'light', 'cam', 'sim'])
