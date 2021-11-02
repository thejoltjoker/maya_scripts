#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
import json


def main():
    """docstring for main"""
    nodes = {}
    sel = cmds.ls(sl=True)
    for node in sel:
        print node
        nodes[node] = {}
        nodes[node]['type'] = cmds.nodeType(node)

        if cmds.listRelatives(node, s=True):
            shapes = [s for s in cmds.listRelatives(node, s=True)]

        for shape in shapes:
            print shape
            nodes[node]['shapes'] = {}
            nodes[node]['shapes'][shape] = cmds.nodeType(shape)

    return json.dumps(nodes)


if __name__ == '__main__':
    print(main())
