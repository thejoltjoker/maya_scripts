#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    sets = cmds.ls('set*', type='objectSet')
    for s in sets:
        if not cmds.listRelatives(ad=True):
            cmds.delete(s)


if __name__ == '__main__':
    main()
