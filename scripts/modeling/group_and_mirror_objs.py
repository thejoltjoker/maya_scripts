#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    sel = cmds.ls(sl=True)
    sep = '_'
    name = sel[0].split(sep, 1)[0]
    group_name = name + '_grp'
    mirrorGroupName = name + 'Mirrored_grp'

    # Group objects
    cmds.group(em=True, n=group_name)
    parent = cmds.listRelatives(sel[0], p=True)
    cmds.parent(group_name, parent)
    for obj in sel:
        cmds.parent(obj, group_name)

    # Duplicate group and mirror
    cmds.duplicate(group_name, n=mirrorGroupName)
    cmds.setAttr(mirrorGroupName + '.scaleX', -1)
    cmds.makeIdentity(mirrorGroupName, apply=True, scale=True)


if __name__ == '__main__':
    main()
