#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
enable_alpha_on_refractive_mtls.py
Description of enable_alpha_on_refractive_mtls.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    for mtl in cmds.ls(type='VRayMtl'):
        if cmds.getAttr('{}.refractionColor'.format(mtl)) != [(0.0, 0.0, 0.0)]:
            try:
                cmds.setAttr('{}.affectAlpha'.format(mtl), 1)
            except:
                print "Couldn't set affected channels"


if __name__ == '__main__':
    main()