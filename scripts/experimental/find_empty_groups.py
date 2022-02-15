#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def find_empty_groups(select=True, delete=False):
    sel = cmds.ls(selection=True)
    nodes = []
    for s in sel:
        rel = cmds.listRelatives(s, allDescendents=True, fullPath=True, type='transform')
        rel_sorted = sorted(rel, key=len, reverse=True)
        for r in rel_sorted:
            children = cmds.listRelatives(r, allDescendents=True, fullPath=True)
            if not children:
                nodes.append(r)

    if select:
        cmds.select(nodes)
    if delete:
        cmds.delete(nodes)

    return nodes


def main():
    find_empty_groups(delete=True)


if __name__ == '__main__':
    main()
