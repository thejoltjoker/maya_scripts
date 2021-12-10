#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import re
import maya.cmds as cmds
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


def remove_suffix(input_string):
    result = re.findall(r'([^\s]+)_\w*$', input_string)
    if result:
        return result[0]
    return input_string


def main():
    """docstring for main"""
    nodes = cmds.ls(type='shadingEngine')

    # Remove defaults from list
    for n in ['initialParticleSE', 'initialShadingGroup']:
        if n in nodes:
            nodes.pop(nodes.index(n))

    for sg in nodes:
        # Get material name
        material_name = remove_suffix(sg)

        # Create redshift material
        material = cmds.shadingNode('RedshiftMaterial', name='{}_shd'.format(material_name), asShader=True)

        # Connect material to shading group
        cmds.connectAttr('{}.outColor'.format(material), '{}.surfaceShader'.format(sg), f=True)


if __name__ == '__main__':
    main()
