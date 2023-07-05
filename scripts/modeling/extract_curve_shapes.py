#!/usr/bin/env python3
"""extract_curve_shapes.py
Extract all curves shapes and put in their own transform
"""
from maya import cmds


def extract_curve_shapes(node):
    new_nodes = []
    for shape in cmds.listRelatives(shapes=True):
        name = '_'.join([node, shape])
        parent = cmds.createNode('transform', name=name)
        cmds.parent(shape, parent, shape=True)
        new_nodes.append(parent)
    return new_nodes


def main():
    """docstring for main"""
    for node in cmds.ls(sl=True):
        extract_curve_shapes(node)


if __name__ == '__main__':
    main()
