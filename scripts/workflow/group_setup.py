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
    nodes = []
    if suffix_uppercase:
        suffix = suffix.upper()

    # Create parent group
    parent = add_suffix(parent, suffix, sep)
    cmds.group(em=True, name=parent)
    nodes.append(parent)

    # create groups
    for n in groups:
        group = cmds.group(em=True, name=add_suffix(n, suffix, sep))
        cmds.parent(group, parent)

        nodes.append(group)

    # lock group attributes
    for n in nodes:
        cmds.setAttr(n + '.translateX', lock=True)
        cmds.setAttr(n + '.translateY', lock=True)
        cmds.setAttr(n + '.translateZ', lock=True)
        cmds.setAttr(n + '.scaleX', lock=True)
        cmds.setAttr(n + '.scaleY', lock=True)
        cmds.setAttr(n + '.scaleZ', lock=True)
        cmds.setAttr(n + '.rotateX', lock=True)
        cmds.setAttr(n + '.rotateY', lock=True)
        cmds.setAttr(n + '.rotateZ', lock=True)


def main():
    create_groups('scene', ['geo', 'light', 'cam', 'sim'])


if __name__ == '__main__':
    main()
