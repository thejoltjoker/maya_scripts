#!/usr/bin/env python3
"""auto_create_controls.py
Description of auto_create_controls.py.
"""
import maya.cmds as cmds

def main():
    """docstring for main"""

    # Get the reference node
    reference_node = cmds.polyCube()

    # Loop through all selected nodes
    for selected_node in cmds.ls(selection=True):
        # Get the X position of the selected node and the reference node
        selected_node_pos = cmds.xform(selected_node, query=True, translation=True, worldSpace=True)
        reference_node_pos = cmds.xform(reference_node, query=True, translation=True, worldSpace=True)
        selected_node_x = selected_node_pos[0]
        reference_node_x = reference_node_pos[0]

        # Create a bounding box around the selected node
        bbox = cmds.exactWorldBoundingBox(selected_node)

        # Create a cube with the same dimensions as the bounding box
        width = bbox[3] - bbox[0]
        height = bbox[4] - bbox[1]
        depth = bbox[5] - bbox[2]
        cube = cmds.polyCube(width=width, height=height, depth=depth)[0]

        # Move the cube to the center of the bounding box
        center_x = (bbox[3] + bbox[0]) / 2
        center_y = (bbox[4] + bbox[1]) / 2
        center_z = (bbox[5] + bbox[2]) / 2
        cmds.move(center_x, center_y, center_z, cube, absolute=True)

        # Color the cube red if it's right of the reference node, blue if it's left of the reference node, yellow if it's not on either side
        if selected_node_x < reference_node_x:
            cmds.setAttr(cube + ".overrideColor", 13)  # Red
        elif selected_node_x > reference_node_x:
            cmds.setAttr(cube + ".overrideColor", 6)  # Blue
        else:
            cmds.setAttr(cube + ".overrideColor", 17)  # Yellow

        # Set the cube to display as a bounding box
        cmds.setAttr(cube + ".overrideEnabled", 1)
        cmds.setAttr(cube + ".overrideLevelOfDetail", 1)

        # Select the cube
        cmds.select(cube, add=True)

    # Deselect all nodes
    cmds.select(clear=True)

if __name__ == '__main__':
    main()