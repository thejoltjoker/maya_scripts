#!/usr/bin/env python3
"""replace_default_shader.py
Description of replace_default_shader.py.
"""
from maya import cmds


def create_material(name):
    """Create a material and return the material and shading group

    Args:
        name: The name of the new material

    Returns:
        tuple: (material, shading group)
    """
    material = cmds.shadingNode('RedshiftMaterial', name='{}_shd'.format(name), asShader=True)
    sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='{}_sg'.format(name))
    cmds.connectAttr('{}.outColor'.format(material), '{}.surfaceShader'.format(sg), f=True)

    return material, sg


def connect_to_sg(nodes: list, sg):
    """Connect nodes to a shading group

    Args:
        nodes: list of nodes
        sg: shading group node
    """
    for node in nodes:
        cmds.sets(node, e=True, forceElement=sg)


def connected_to_initial_shading_group():
    """Get all nodes connected to initialShadingGroup

    Returns:
        list: list of nodes connected to initialShadingGroup
    """
    connected = cmds.listConnections('initialShadingGroup')
    transforms = [x for x in connected if cmds.nodeType(x) == 'transform']
    return transforms


def main():
    """docstring for main"""
    # Find all objects attached to default shader
    nodes = connected_to_initial_shading_group()
    # Create new material
    material, sg = create_material('default')
    # Apply material to objects
    connect_to_sg(nodes, sg)


if __name__ == '__main__':
    main()
