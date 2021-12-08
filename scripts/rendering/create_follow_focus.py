#!/usr/bin/env python
"""
create_follow_focus.py
Description of create_follow_focus.py.
"""
import os
import maya.cmds as cmds


def create_follow_focus():
    sel_nodes = cmds.ls(sl=True)

    if sel_nodes:
        for node in sel_nodes:
            if cmds.nodeType(cmds.listRelatives(node)) == 'camera':
                cam_shape = cmds.listRelatives(shapes=True)
                camera_position = cmds.camera(sel_nodes[0], p=True, q=True)
                camera_position[2] = int(camera_position[2]) - 10
                distance_node_shape = cmds.distanceDimension(
                    sp=(0, 0, 456), ep=camera_position)
                distance_node_loc_cam, distance_node_loc_focal = cmds.listConnections(
                    distance_node_shape)
                distance_node_loc_cam = cmds.rename(distance_node_loc_cam,
                                                    sel_nodes[0] + "FFCam_LOC")
                distance_node_loc_focal = cmds.rename(
                    distance_node_loc_focal, sel_nodes[0] + "FFFocalPt_LOC")
                distance_node = cmds.rename(
                    cmds.listRelatives(distance_node_shape, p=True),
                    sel_nodes[0] + "FFDistance_DIST")

                # Set color of the focus plane locator
                cmds.setAttr(distance_node_loc_focal + ".overrideEnabled", 1)
                cmds.setAttr(distance_node_loc_focal + ".overrideColor", 18)

                cmds.parentConstraint(
                    sel_nodes[0], distance_node_loc_cam, maintainOffset=False)
                cmds.aimConstraint(
                    sel_nodes[0],
                    distance_node_loc_focal,
                    maintainOffset=False)

                # Lock and hide translation and rotation for cam locator
                lock_attributes = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']
                for attr in lock_attributes:
                    cmds.setAttr(
                        distance_node_loc_cam + attr,
                        lock=True,
                        keyable=False,
                        channelBox=False)

                cmds.group(
                    distance_node_loc_cam,
                    distance_node_loc_focal,
                    distance_node,
                    n=sel_nodes[0] + "FollowFocus_GRP")

                for shape in cam_shape:
                    cmds.connectAttr(distance_node + '.distance',
                                     shape + '.focusDistance')
            else:
                cmds.warning("No cameras are selected")
    else:
        cmds.warning("Nothing is selected")


def main():
    create_follow_focus()


if __name__ == '__main__':
    main()
