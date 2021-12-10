#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
delete_object_sets.py
Delete empty object sets.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    obj_set_list = cmds.ls('set*', type='objectSet')
    for obj in obj_set_list:
        if cmds.objectType(obj, isType='objectSet'):
            if not cmds.listRelatives(obj, c=True):
                cmds.delete(obj)


if __name__ == '__main__':
    main()
