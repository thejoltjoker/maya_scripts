#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import re
import maya.cmds as cmds


def remove_suffix(input_string):
    result = re.findall(r'([^\s]+)_\w*$', input_string)
    if result:
        print(result)
        return result[0]
    return input_string


def main():
    """docstring for main"""
    for node in cmds.ls(sl=True):
        # Create material
        name = node
        material = cmds.shadingNode('RedshiftMaterial', name='{}_shd'.format(name), asShader=True)
        sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='{}_sg'.format(name))

        cmds.connectAttr('{}.outColor'.format(material), '{}.surfaceShader'.format(sg), f=True)
        # assignCreatedShader "RedshiftMaterial" "" rsMaterial6 "polySurface27";
        cmds.sets(node, e=True, forceElement=sg)


if __name__ == '__main__':
    main()
