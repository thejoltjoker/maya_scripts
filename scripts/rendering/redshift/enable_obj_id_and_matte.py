#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
enable_obj_id_and_matte.py
Description of enable_obj_id_and_matte.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    for i in cmds.ls(type='RedshiftProxyMesh'):
        cmds.setAttr('{}.visibilityMode'.format(i), 1)
        cmds.setAttr('{}.objectIdMode'.format(i), 1)
        print('Object ID and Matte overrides enabled for {}'.format(i))


if __name__ == '__main__':
    main()
