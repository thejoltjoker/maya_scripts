#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
list_material_textures.py
Description of list_material_textures.py.
"""
import maya.cmds as cmds
import json


def main():
    """docstring for main"""
    materials = cmds.ls(mat=True)
    dict = {}
    for mat in materials:
        dict[mat] = {}
        dict[mat]['type'] = cmds.nodeType(mat)
        dict[mat]['maps'] = {}
        in_conn = cmds.listConnections(
            mat, s=True, d=False, c=True, scn=True, t='file')
        if in_conn is not None:
            for n, node in enumerate(in_conn):
                if n % 2 == 0:
                    dict[mat]['maps'][node] = cmds.getAttr(
                        '{}.fileTextureName'.format(in_conn[n+1]))
                else:
                    pass  # Odd
    print(json.dumps(dict))


if __name__ == '__main__':
    main()
