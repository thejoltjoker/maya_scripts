#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def has_children(node):
    children = cmds.listRelatives(node, allDescendents=True, fullPath=True)
    if children:
        return True
    return False


def delete_empty_groups():
    sel = cmds.ls(selection=True)
    nodes = []
    for s in sel:
        rel = cmds.listRelatives(s, allDescendents=True, fullPath=True, type='transform')
        rel_sorted = sorted(rel, key=len, reverse=True)

        # Delete children
        for r in rel_sorted:
            if not has_children(r):
                nodes.append(r)
                cmds.delete(r)

        # Delete top level
        if not has_children(s):
            nodes.append(s)
            cmds.delete(s)

    return nodes


if __name__ == '__main__':
    delete_empty_groups()
