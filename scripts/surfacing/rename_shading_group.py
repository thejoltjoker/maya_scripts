#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rename_shading_group.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    selection = cmds.ls(sl=True, type='shadingEngine')

    for node in selection:
        material = cmds.listConnections(
            '{}.surfaceShader'.format(node), d=False, s=True)[0]
        if material.endswith('_MTL'):
            material = material.replace('_MTL', 'Mtl').replace('_MAT', 'Mat')

        new_name = '{}_SG'.format(material)

        cmds.rename(node, new_name)


if __name__ == '__main__':
    main()
