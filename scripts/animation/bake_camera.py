#!/usr/bin/env python3
"""bake_camera.py
Description of bake_camera.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    # Get the selected camera
    selected_cameras = cmds.ls(selection=True, type='camera')
    if not selected_cameras:
        cmds.warning('Please select a camera.')
        raise ValueError('No camera selected.')

    camera = selected_cameras[0]

    # Get the camera's transform node
    transform = cmds.listRelatives(camera, parent=True)[0]

    # Bake the camera's animation
    cmds.bakeResults(transform, simulation=True,
                     t=(cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True)))

    # Remove any connections to other nodes
    connections = cmds.listConnections(camera, plugs=True, connections=True)
    if connections:
        for i in range(0, len(connections), 2):
            cmds.disconnectAttr(connections[i + 1], connections[i])

    print('Camera baked and disconnected from other nodes.')


if __name__ == '__main__':
    main()
