#!/usr/bin/env python3
"""move_away_from_center.py
Description of move_away_from_center.py.
"""
import maya.cmds as cmds
import math


def main():
    """docstring for main"""

    # Get the center of the scene
    center = [0, 0, 0]

    # Get the selected objects
    selected = cmds.ls(selection=True)

    # Set the distance to move the objects
    distance = 5  # Change this to adjust the distance to move the objects

    # Loop through the selected objects
    for obj in selected:
        # Get the object's position
        pos = cmds.xform(obj, query=True, worldSpace=True, translation=True)

        # Calculate the distance from the center
        dist = math.sqrt((pos[0] - center[0]) ** 2 + (pos[1] - center[1]) ** 2 + (pos[2] - center[2]) ** 2)

        # Move the object away from the center based on its distance
        if dist != 0:
            cmds.move(pos[0] + (pos[0] - center[0]) / dist * distance, pos[1] + (pos[1] - center[1]) / dist * distance,
                      pos[2] + (pos[2] - center[2]) / dist * distance, obj, relative=True)


if __name__ == '__main__':
    main()
