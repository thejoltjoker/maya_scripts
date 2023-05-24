#!/usr/bin/env python3
""".py
Description of .py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    # Get the selected node and the reference node
    selected_node = cmds.ls(selection=True)[0]
    reference_node = "pCube1"  # Replace with the name of your reference node

    # Get the X position of the selected node and the reference node
    selected_node_pos = cmds.xform(selected_node, query=True, translation=True, worldSpace=True)
    reference_node_pos = cmds.xform(reference_node, query=True, translation=True, worldSpace=True)
    selected_node_x = selected_node_pos[0]
    reference_node_x = reference_node_pos[0]

    # Check if the selected node is left or right of the reference node
    if selected_node_x < reference_node_x:
        print(selected_node + " is left of " + reference_node)
    else:
        print(selected_node + " is right of " + reference_node)


if __name__ == '__main__':
    main()
