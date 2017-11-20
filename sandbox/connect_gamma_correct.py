#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
connect_gamma_correct.py
Description of connect_gamma_correct.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    texture_node = cmds.ls(sl=True, type='file')[0]
    gamma_node = cmds.shadingNode('gammaCorrect', asUtility=True)
    # // Result: gammaCorrect7 //
    # defaultNavigation -ce -source LEGA_01_LEGA_01_050_Lay:Jack_Rig:jck_sleeve_texture_color1 -destination gammaCorrect7.value;
    cmds.connectAttr(
        '{}.outColor'.format(texture_node),
        '{}.value'.format(gamma_node),
        force=True)


if __name__ == '__main__':
    main()
